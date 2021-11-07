#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import Prime


def encryption(message: int, puk: list) -> int:
    return Prime.quick_pow_mod(message, puk[1], puk[0])


def decryption(secret: int, prk: list) -> int:
    return Prime.quick_pow_mod(secret, prk[1], prk[0])


def get_RSAKey():
    RSAKey = {}
    prime_arr: list = Prime.get_rand_prime_arr(2)
    p: int = prime_arr[0]
    q: int = prime_arr[1]
    while p == q:
        q = random.choice(prime_arr)
    n: int = p * q
    s: int = (p - 1) * (q - 1)
    e: int = 65537
    d: int = Prime.mod_inverse(e, s)
    print("Private Key:")
    print("N:")
    print(n)
    print("d:")
    print(d)
    print("Public Key:")
    print("N:")
    print(n)
    print("e:")
    print(e)
    puk: list = [n, e]
    prk: list = [n, d]
    RSAKey['puk'] = puk
    RSAKey['prk'] = prk
    return RSAKey


if __name__ == '__main__':
    RSAKey: [str, list] = get_RSAKey()
    message: int = int(input())
    secret: int = encryption(message, RSAKey['puk'])
    print("Ciphertext:")
    print("c:")
    print(secret)
    message: int = decryption(secret, RSAKey['prk'])
    print("Plaintext:")
    print("m':")
    print(message)
    print("insecure")
