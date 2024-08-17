#!/usr/bin/env python3
"""
Script Name: data_type_classification.py
Description: 
    This script shows all built-in data type.
Usage:
    $ python3 data_type_classification.py

Author: tatsujin
Date: 2024-08-11
"""

# Header title, column max width (tuple list)
headers = [
    ("Built-in Types", 20),
    ("Data Container", 15),
    ("Sequence", 10),
    ("Mapping", 8),
    ("Iterable", 8),
    ("Mutable", 8),
    ("Immutable", 10),
    ("Data", 20),
]

data_type_classification = {
    "int": ("", "", "", "", "", "◎", "Integer"),
    "float": ("", "", "", "", "", "◎", "Floating-point number"),
    "complex": ("", "", "", "", "", "◎", "Complex number"),
    "bool": ("", "", "", "", "", "◎", "True, False"),
    "NoneType": ("", "", "", "", "", "◎", "None"),
    "str": ("", "◎", "", "◎", "", "◎", "String"),
    "range": ("", "◎", "", "◎", "", "◎", "Integer sequence"),
    "list": ("◎", "◎", "", "◎", "◎", "", "List"),
    "tuple": ("◎", "◎", "", "◎", "", "◎", "Tuple"),
    "set": ("◎", "", "", "◎", "◎", "", "Set"),
    "frozenset": ("◎", "", "", "◎", "", "◎", "Immutable set"),
    "dict": ("◎", "", "◎", "◎", "◎", "", "Dictionary"),
    "bytes": ("", "◎", "", "◎", "", "◎", "Byte sequence"),
    "bytearray": ("", "◎", "", "◎", "◎", "", "Mutable byte sequence"),
    "memoryview": ("", "", "", "◎", "◎", "", "Memory view"),
}


def print_classification_table():
    format_str = " | ".join([f"{{:<{width}}}" for _, width in headers])
    separator = "-+-".join(["-" * width for _, width in headers])

    # Print header and separator
    header_titles = [title for title, _ in headers]
    print(format_str.format(*header_titles))
    print(separator)

    # Print each data
    for data_type, attributes in data_type_classification.items():
        print(format_str.format(data_type, *attributes))


def show_int():
    i = 1729
    print(f"{type(i)} {i}")


def show_float():
    f = 3.14
    print(f"{type(f)} {f}")


def show_complex():
    c = 2 + 3j
    print(f"{type(c)} {c}")


def show_bool():
    b1 = True
    b2 = False
    print(f"{type(b1)} {b1}, {b2}")


def show_none():
    n = None
    print(f"{type(n)} {n}")


def show_str():
    s = "Hello, World!"
    print(f"{type(s)} {s}")


def show_range():
    r = range(0, 10, 2)  # Create even number
    print(f"{type(r)} {list(r)}")


def show_list():
    lst = [1, 1, 2, 3, 5, 8, 13]
    lst.append(20)
    lst[7] = 21  # List type is mutable
    print(f"{type(lst)} {lst}")


def show_tuple():
    t = (1, 1, 2, 3, 5, 8, 13)
    # t[1] = 21  # This is error, tuple type is immutable
    print(f"{type(t)} {t}")


def show_dict():
    d = {"one": 1, "two": 2, "three": 3}
    d["four"] = 4
    print(f"{type(d)} {d}")


def show_set():
    # Since it is a set type, duplicate elements is deleted
    s = {1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7}
    s.add(8)  # Set type is mutable
    s.add(2)
    print(f"{type(s)} {s}")


def show_frozenset():
    # Since it is a set type, duplicate elements is deleted
    fs = frozenset({1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7})
    # fs.add(8)  # This is error, frozen set type is immutable
    print(f"{type(fs)} {fs}")


def show_bytes():
    b = b"hello"
    print(f"{type(b)} {b}")


def show_bytearray():
    ba = bytearray(b"hello")
    ba[0] = ord("H")  # Bytesrray type is mutable, convert uppercase: h => H
    print(f"{type(ba)} {ba}")


def show_memoryview():
    # To indicate an address like a pointer, memoryview type is more memory efficient.
    b = b"hello"
    mv = memoryview(b)
    print(f"{type(mv)} {mv} {mv.tobytes()}")


def main():
    print("[Classification table]")
    print_classification_table()

    print("\n[Numerical data types]")
    show_int()
    show_float()
    show_complex()

    print("\n[Special data types]")
    show_bool()
    show_none()

    print("\n[Sequence data types]")
    show_str()
    show_range()
    show_list()
    show_tuple()

    print("\n[Mapping data type]")
    show_dict()

    print("\n[Set data type]")
    show_set()
    show_frozenset()

    print("\n[Binary data types]")
    show_bytes()
    show_bytearray()
    show_memoryview()


if __name__ == "__main__":
    main()
