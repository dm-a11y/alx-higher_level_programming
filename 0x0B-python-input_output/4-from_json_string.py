#!/usr/bin/python3
'''
a function that returns an object (Python data structure) represented by a JSON string
'''

import json



def from_json_string(my_str):
    '''
    module from_json_string
    returns python objects
    '''
    return json.loads(my_str)

