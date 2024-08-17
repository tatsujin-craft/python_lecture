#!/usr/bin/env python3
"""
Script Name: sample.py
Description: 
    This script handles multiple input lines.

Usage:
    $ python3 sample.py

Author: tatsujin
Date: 2024-08-10
"""

import sys


def read_lines_with_input_func():
    num = int(input())
    lines_num = int(input())
    result_list = []
    for _ in range(lines_num):
        # Convert the input line into uppercase and split by commas
        input_line_list = [item.upper() for item in input().strip().split(",")]
        # Store the result in the 2D list
        result_list.append(input_line_list)
    return num, lines_num, result_list


def read_lines_with_sys_func():
    # Read all input from stdin and strip any surrounding whitespace
    input_lines_str = sys.stdin.read().strip()
    # Split the input into lines
    input_lines = input_lines_str.splitlines()
    num = int(input_lines[0])
    lines_num = int(input_lines[1])

    result_list = []
    # Process each line after the first two
    begin_line = 2
    for line in input_lines[begin_line : begin_line + lines_num]:
        # Convert the input line into uppercase and split by commas
        input_line_list = [item.upper() for item in line.strip().split(",")]
        # Store the result in the 2D list
        result_list.append(input_line_list)

    return num, lines_num, result_list


def main():
    """
    Main function that handles input and output.
    """

    # Read input lines
    sys_mode = False
    if sys_mode:
        print("Use function: sys.stdin.read()")
        num, lines_num, result_list = read_lines_with_sys_func()
    else:
        print("Use function: input()")
        num, lines_num, result_list = read_lines_with_input_func()

    # Output all results
    print("[Result]")
    print(f"Number: {num}, Lines: {lines_num}")
    marine_animals = result_list[0]
    print(f"Marine animals: {marine_animals}")
    land_animals = result_list[1]
    print(f"Land animals: {land_animals}")
    sky_animals = result_list[2]
    print(f"Sky animals: {sky_animals}")


if __name__ == "__main__":
    main()
