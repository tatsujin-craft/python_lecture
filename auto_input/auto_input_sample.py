#!/usr/bin/env python3
"""
Script Name: auto_input_sample.py
Description: 
    This script runs sample.py with automatic input.
Usage:
    $ python3 auto_input_sample.py

Author: tatsujin
Date: 2024-08-10
"""

import subprocess


def run_with_auto_input(script_name, inputs):
    """
    This function runs python script with automatic input.
    """
    # Combine all inputs into a single string separated by newlines
    input_data = "\n".join(inputs)

    # Run the script with the input piped to it
    process = subprocess.Popen(
        ["python3", script_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(input=input_data.encode())

    # Print the output from the script
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


def main():
    # Input data to simulate
    inputs = [
        "100",
        "3",
        "penguin,dolphin,whale,orca",
        "lion,tiger,wolf,bear",
        "eagle,falcon,swallow",
    ]

    # Name of the script to run
    script_name = "sample.py"

    # Call the function to simulate input and run the script
    run_with_auto_input(script_name, inputs)


if __name__ == "__main__":
    main()
