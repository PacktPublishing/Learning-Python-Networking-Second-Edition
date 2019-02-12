#call libraries
import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])

# initialize objects
loader = DataLoader()
options = Options(connection='local', module_path='', forks=100, become=None, become_method=None, become_user=None, check=False,
                  diff=False)
passwords = dict(vault_pass='secret')

# create inventory
inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create play with task
play_source = dict(
        name = "mypythoncheck",
        hosts = 'myrouters',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='hostname'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# execution
task = None
try:
    task = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
              stdout_callback='default'
          )
    result = task.run(play)
finally:
    if task is not None:
        task.cleanup()
