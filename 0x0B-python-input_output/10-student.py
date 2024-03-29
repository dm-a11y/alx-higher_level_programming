#!/usr/bin/python3

'''
a class Student that defines a student by: (based on 9-student.py)
'''

class Student:
    '''
    class module student
    '''

    def __init__(self, first_name, last_name, age):
        '''
        initialize a new student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            '''
            Get a dictionary representation of the Student.
            If attrs is a list of strings, represents only
            those attributesincluded in the list.

            Args:
                attrs (list): (optional) the attributes to
                represent.
            '''

            if (type(attrs) == list and
                    all(type(ele) == str for ele in attrs)):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
