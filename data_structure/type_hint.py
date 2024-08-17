#!/usr/bin/env python3
"""
Script Name: type_hint.py
Description: 
    This script tests type hint.
Usage:
    $ python3 type_hint.py

Author: tatsujin
Date: 2024-08-11
"""

from typing import List, Dict, Tuple, Union, Optional, NamedTuple
from dataclasses import dataclass


# Class
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# Dataclass
@dataclass
class PointDC:
    x: int
    y: int


# NamedTuple
class PointNT(NamedTuple):
    x: int
    y: int


def get_sum(a: int, b: int) -> int:
    return a + b


def get_product(value: Union[int, float]) -> float:
    return float(value) * 1.5


def get_longest_name(items: List[str]) -> Tuple[int, str]:
    count = len(items)
    longest = max(items, key=len)
    return count, longest


def find_item(items: List[str], keyword: str) -> Optional[str]:
    for item in items:
        if keyword in item:
            return item
    return None


def get_user_info(user_id) -> Dict[str, Union[str, int]]:
    user_info = {"id": user_id, "name": f"User_{user_id}", "age": 30}
    return user_info


# Class
def calculate_distance(point1: Point, point2: Point) -> float:
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5


# Dataclass
def calculate_distance_dc(point1: PointDC, point2: PointDC) -> float:
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5


# NamedTuple
def calculate_distance_nt(point1: PointNT, point2: PointNT) -> float:
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5


def main():
    sum = get_sum(5, 3)
    print(f"Sum: {sum}")

    product1 = get_product(10)
    product2 = get_product(10.5)
    print(f"Product1: {product1}")
    print(f"Product2: {product2}\n")

    items_list = ["lion", "tiger", "wolf", "bear"]
    result_tuple = get_longest_name(items_list)
    print(f"Longest name: {result_tuple}")

    found_item = find_item(items_list, "on")
    print(f"Found item: {found_item}")

    user_dict = get_user_info(user_id=10)
    print(f"User info: {user_dict}\n")

    # Class
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    distance = calculate_distance(p1, p2)
    print(f"Distance (class): {distance} m")

    # Dataclass
    p1_dc = PointDC(1, 2)
    p2_dc = PointDC(4, 6)
    distance_dc = calculate_distance_dc(p1_dc, p2_dc)
    print(f"Distance (dataclass): {distance_dc} m")

    # NamedTuple
    p1_nt = PointNT(1, 2)
    p2_nt = PointNT(4, 6)
    distance_nt = calculate_distance_nt(p1_nt, p2_nt)
    print(f"Distance (NamedTuple): {distance_nt} m")


if __name__ == "__main__":
    main()
