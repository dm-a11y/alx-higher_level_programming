#!/usr/bin/python3
'''
funtion that inherits from the list
'''

class MyList(list):
    """Mylist class that inherits from list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
