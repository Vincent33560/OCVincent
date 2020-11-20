#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

def main():

	module = AnsibleModule(argument_spec={})
	response = {"result" : "hello world"}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
	main()