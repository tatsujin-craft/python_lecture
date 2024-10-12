#!/usr/bin/env python3


# AND演算
def bitwise_and(a, b):
    return a & b


# OR演算
def bitwise_or(a, b):
    return a | b


# XOR演算
def bitwise_xor(a, b):
    return a ^ b


# NOT演算
def bitwise_not(a):
    return ~a


# 左シフト
def shift_left(a, n):
    return a << n


# 右シフト
def shift_right(a, n):
    return a >> n


# メイン処理
def main():
    a = 0b1101  # 13 (2進数)
    b = 0b1011  # 11 (2進数)

    print(
        f"AND演算: {bin(a)} & {bin(b)} = {bin(bitwise_and(a, b))} ({bitwise_and(a, b)})"
    )
    print(f"OR演算: {bin(a)} | {bin(b)} = {bin(bitwise_or(a, b))} ({bitwise_or(a, b)})")
    print(
        f"XOR演算: {bin(a)} ^ {bin(b)} = {bin(bitwise_xor(a, b))} ({bitwise_xor(a, b)})"
    )
    print(f"NOT演算: ~{bin(a)} = {bin(bitwise_not(a))} ({bitwise_not(a)})")
    print(f"左シフト: {bin(a)} << 2 = {bin(shift_left(a, 2))} ({shift_left(a, 2)})")
    print(f"右シフト: {bin(a)} >> 2 = {bin(shift_right(a, 2))} ({shift_right(a, 2)})")


if __name__ == "__main__":
    main()
