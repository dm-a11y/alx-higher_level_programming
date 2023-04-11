#!/usr/bin/python3
'''
a function that that checks a class
'''

def is_same_class(obj, a_class):
    '''
    To check if the object is exactly an instance of the specified class
        Args:
            obj: initial object
            a_class: class to confirm with the object
            Returns: true if the object is an instance  or if the object is 
            an instance of a class that inherited from, the specified class ; otherwise False.

    if type(obj) == a_class:
        return True
    return False
