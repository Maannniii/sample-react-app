#!/usr/bin/env python

DOCUMENTATION = '''
---
module: json_data

short_description: Code to Update/Format JSON.

version_added: "2.7"

description:
    - "The module creates json file in the given path if not exists. 
       If exists then it is updated and formatted. 
       Please note that the parent dir will be creaed if it doesn't exists."

options:
    path:
        description:
            - JSON file path.
        required: true
    values:
        description:
            - Values to update in JSON File.
        required: true


author:
    - Mani M (@manim)
'''

EXAMPLES = '''
# Pass in a message

- name: Create andUpdate JSON file.
  json_data: 
    path: "/path/file.json"
    values: >
            {
             "key1" : ["value1", "value2"],
             "key2" : "value3"
             }

'''

import json
import os

from ansible.module_utils.basic import AnsibleModule


def formatandsave(path, values):
    changed = False
    data = json.loads(open(path).read().strip())
    for key in values.keys():
        if data.get(key, "") != values.get(key):
            data[key] = values.get(key)
            changed = True
    json.dump(data, open(path, "w"), sort_keys=True, indent=4, separators=(',', ': '))
    return changed


def firstProg(path, values):
    if (os.path.exists(path)):
        formatandsave(path, values)
    else:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        open(path, "w").write("{}")
    return formatandsave(path, values)


if __name__ == '__main__':
    module = AnsibleModule(argument_spec=dict(path=dict(required=True, type=str), values=dict(required=True, type=str)
                                              ))
    path = module.params.get('path')
    values = json.loads(module.params.get('values'))
    result = firstProg(path, values)
    module.exit_json(changed=True, msg="ok") if result else module.exit_json(changed=False, msg="Key value pair exists")

