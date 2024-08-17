#!/usr/bin/env python3
"""
Script Name: slice_object.py
Description: 
    This script tests slice syntax of object[a:b].
Usage:
    $ python3 slice_object.py

Author: tatsujin
Date: 2024-08-11
"""


def slice_object_with_syntax(numbers):
    print("\nUse [a:b:c] syntax")
    first_slice = numbers[0:3]
    print("First slice:", first_slice)

    middle_slice = numbers[3:7]
    print("Middle slice:", middle_slice)

    last_slice = numbers[-3:]
    print("Last slice:", last_slice)

    even_numbers = numbers[1::2]
    print("Even index numbers:", even_numbers)

    reverse_numbers = numbers[::-1]
    print("Reversed list:", reverse_numbers)


def slice_object_with_function(numbers):
    print("\nUse slice(a,b,c) function")
    slice_object = slice(3, 7)
    middle_slice = numbers[slice_object]
    print("Middle slice:", middle_slice)

    slice_object = slice(1, None, 2)
    even_numbers = numbers[slice_object]
    print("Even index numbers:", even_numbers)


def delete_slice_object(numbers):
    numbers[2:8] = []
    print("\nMiddle deleted list", numbers)


def main():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Source list: ", numbers)
    slice_object_with_syntax(numbers)
    slice_object_with_function(numbers)
    delete_slice_object(numbers)


if __name__ == "__main__":
    main()
