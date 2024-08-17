#!/usr/bin/env python3
"""
Script Name: enumerate.py
Description: 
    This script tests function of enumerate().
Usage:
    $ python3 enumerate.py

Author: tatsujin
Date: 2024-08-11
"""


def main():
    animals = ["lion", "tiger", "wolf", "bear"]

    for index, animal in enumerate(animals, start=1):
        print(f"Index: {index}, Animal: {animal}")


if __name__ == "__main__":
    main()
