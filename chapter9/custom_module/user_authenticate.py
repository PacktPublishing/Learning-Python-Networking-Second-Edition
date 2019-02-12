#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule

def main():

    data = {"host": {"default": "localhost”, "type": "str"},
	"username": {"default": "username", "type": "str"},
	"password": {"default": "password", "type": "str"},
	"url": {"default": "url", "type": "str"}
	}

	module = AnsibleModule(argument_spec = data)

    host = module.params.get('host')
	username = module.params.get('username')
	password = module.params.get('password')
	url='http://' + host + '/authentication'
	
	module.params.update({"url": url})
    module.exit_json(changed=True, meta=module.params)


if __name__ == '__main__':
    main()