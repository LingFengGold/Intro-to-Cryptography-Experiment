#!/usr/bin/env python3 

import base64


def bytes_to_hex(in_bytes: bytes) -> None:
    print("hexadecimal integers:", end=' ')
    print(in_bytes.hex())


def encode_base64(in_bytes: bytes) -> None:
    print("Base64_str:", end=' ')
    print((base64.b64encode(in_bytes)).decode('utf-8'))


def encrypt(plaintext: bytes, keyword: bytes) -> bytes:
    ans: bytes = b''
    for i in range(0, len(plaintext)):
        b: int = (plaintext[i] + keyword[i]) % 256
        ans = ans + b.to_bytes(length=1, byteorder='big', signed=False)
    return ans


hex_string: str = input("Please input a hex string:")
plaintext_array: bytes = bytes.fromhex(hex_string)
hex_string: str = input("Please input a hex string:")
keyword_array: bytes = bytes.fromhex(hex_string)

ciphertext_array: bytes = encrypt(plaintext_array, keyword_array)
bytes_to_hex(ciphertext_array)
encode_base64(ciphertext_array)
