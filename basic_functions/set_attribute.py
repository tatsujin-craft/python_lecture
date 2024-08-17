#!/usr/bin/env python3
"""
Script Name: set_attribute.py
Description: 
    This script tests function of setattr(), getattr().
Usage:
    $ python3 set_attribute.py

Author: tatsujin
Date: 2024-08-11
"""


class Person:
    def __init__(self, name):
        self.name = name


def main():
    # Create instance
    person = Person("Taro")

    # Set attribute dynamically
    setattr(person, "age", 30)
    setattr(person, "city", "Tokyo")

    # Get default attribute
    name = getattr(person, "name")
    print(f"Name: {name}")

    # Get new attribute
    age = getattr(person, "age")
    city = getattr(person, "city")
    print(f"Age: {age}")
    print(f"City: {city}")

    # Get attribute that does not exist
    country = getattr(person, "country", "Unknown")
    print(f"Country: {country}")


if __name__ == "__main__":
    main()
