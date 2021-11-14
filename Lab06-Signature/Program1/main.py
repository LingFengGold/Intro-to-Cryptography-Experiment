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
    # Generate a textbook RSA key pair. Print the private key and the public key as multiple decimal strings.
    RSAKey: [str, list] = get_RSAKey()

    # Read a decimal string representing a plaintext message . Raise an exception if is invalid.
    message: int = int(input())

    # Sign the message . Print the signature as a decimal string.
    secret: int = encryption(message, RSAKey['prk'])
    print("Signature:")
    print("s:")
    print(secret)

    # Verify the signature of message . Print valid if the signature is valid. Print invalid otherwise.
    message1: int = decryption(secret, RSAKey['puk'])
    print("Verify s of m:")
    if message1 == message:
        print("valid")
    else:
        print("invalid")

    # Randomly pick a number as a faked message , and verify the signature s of message m'
    # Print valid if the signature is valid. Print invalid otherwise.
    print("m'(faked):")
    m_fake = Prime.get_rand_prime_arr(2)
    print(m_fake[1])
    secret_fake: int = encryption(m_fake[1], RSAKey['prk'])
    print("Verify s of m':")
    if secret == secret_fake:
        print("valid")
    else:
        print("invalid")

    # Randomly pick a number as a faked signature , and verify the signature s' of message m'
    # Print valid if the signature is valid. Print invalid otherwise.
    print("s'(faked):")
    s_fake = Prime.get_rand_prime_arr(2)
    print(s_fake[1])
    message_fake: int = decryption(s_fake[1], RSAKey['prk'])
    print("Verify s' of m':")
    if message == message_fake:
        print("valid")
    else:
        print("invalid")
