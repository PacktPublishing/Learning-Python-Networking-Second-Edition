#!/usr/bin/env python3

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.playbook_executor import PlaybookExecutor

def execute_playbook():
    playbook_path = "playbook_template.yml"
    inventory_path = "hosts"

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff', 'listhosts', 'listtasks', 'listtags', 'syntax'])
    loader = DataLoader()
    options = Options(connection='local', module_path='', forks=100, become=None, become_method=None, become_user=None, check=False,
                    diff=False, listhosts=False, listtasks=False, listtags=False, syntax=False)
    passwords = dict(vault_pass='secret')

    inventory = InventoryManager(loader=loader, sources=['inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    executor = PlaybookExecutor(  
                playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader,  
                options=options, passwords=passwords)  
    results = executor.run()  
    print results

if __name__ == "__main__":
    execute_playbook()
