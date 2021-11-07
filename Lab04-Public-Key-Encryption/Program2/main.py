#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import Prime


def gcd(a: int, b: int) -> int:
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def gen_key(p: int) -> int:
    key: int = random.randint(pow(10, 154), p)
    while gcd(p, key) != 1:
        key = random.randint(pow(10, 154), p)
    return key


def power(a: int, b: int, c: int) -> int:
    x: int = 1
    y: int = a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c


def encrypt(msg: str, p: int, beta: int, alpha: int) -> [int, list]:
    en_msg: list = []

    i: int = gen_key(p)
    Km: int = power(beta, i, p)
    Ke: int = power(alpha, i, p)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    for i in range(0, len(en_msg)):
        en_msg[i] = Km * ord(en_msg[i])

    return Ke, en_msg


def decrypt(t: list, r: int, a: int, p: int) -> list:
    dr_msg = []
    Km = power(r, a, p)
    for i in range(0, len(t)):
        dr_msg.append(chr(int(t[i] / Km)))

    return dr_msg


def main():
    msg: str = input()
    prime_arr: list = Prime.get_rand_prime_arr(1)
    p: int = prime_arr[0]
    alpha: int = random.randint(2, p)
    a: int = gen_key(p)
    beta: int = power(alpha, a, p)

    print("Private Key:")
    print("p:")
    print(p)
    print("alpha:")
    print(alpha)
    print("a:")
    print(a)
    print("Public Key:")
    print("p:")
    print(p)
    print("alpha:")
    print(alpha)
    print("beta:")
    print(beta)

    r, t = encrypt(msg, p, beta, alpha)

    print("Ciphertext:")
    print("r:")
    print(r)
    print("t:")
    print(t[0])

    dr_msg: list = decrypt(t, r, a, p)
    d_msg: str = ''.join(dr_msg)

    print("Plaintext:")
    print(d_msg)


if __name__ == '__main__':
    main()
