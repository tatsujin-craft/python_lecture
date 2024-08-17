#!/usr/bin/env python3
"""
Script Name: class_variables.py
Description: 
    This script tests class variables.
Usage:
    $ python3 class_variables.py

Author: tatsujin
Date: 2024-07-20
"""


class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
        MyClass.class_variable += 1

    def instance_method(self):
        print(f"\nInstance variable: {self.instance_variable}")
        print(f"Class variable (instance method): {MyClass.class_variable}")

    @classmethod
    def class_method(cls):
        print(f"Class variable (class method): {cls.class_variable}")


if __name__ == "__main__":
    # Create instance
    obj1 = MyClass(1)
    obj2 = MyClass(2)

    # Call instance method
    obj1.instance_method()
    obj2.instance_method()

    # Call class method
    MyClass.class_method()
