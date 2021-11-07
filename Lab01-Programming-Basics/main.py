#!/usr/bin/env python3 
import base64


def bytes_to_dec(in_bytes: bytes) -> None:
    print("decimal integers:", end=' ')
    for b in in_bytes:
        print(b, end=' ')
    print()


def bytes_to_hex(in_bytes: bytes) -> None:
    print("hexadecimal integers:", end=' ')
    for b in in_bytes:
        print(hex(b), end=' ')
    print()


def encode_base64(in_bytes: bytes) -> None:
    print("Base64_str:", end=' ')
    print(base64.b64encode(in_bytes))


def decode_utf8(in_bytes: bytes) -> str:
    print("text_str:", end=' ')
    return in_bytes.decode('utf-8')


hex_string: str = input("Please input a hex string:")

byte_array: bytes = bytes.fromhex(hex_string)
print("byte_array:", byte_array)

bytes_to_dec(byte_array)

bytes_to_hex(byte_array)

encode_base64(byte_array)

hex_string: str = input("Please input a hex_string:")
byte_array: bytes = bytes.fromhex(hex_string)

print(decode_utf8(byte_array))
