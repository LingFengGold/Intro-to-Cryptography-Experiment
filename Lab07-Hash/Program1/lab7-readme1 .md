# readme

## 倪浚桐

## 202022161224

## Lab7-progarm1

## macOS Monterey 12.0.1

## Pycharm 11.0.12 x86-64

## Python 3.9.5

![Screen Shot 2021-11-30 at 7.14.56 PM](/Users/lingfeng/Desktop/Screen Shot 2021-11-30 at 7.14.56 PM.png)

```python
import hashlib
import base64

hex_string: str = input()

byte_array: bytes = bytes.fromhex(hex_string)

# MD5
md5 = hashlib.md5()
md5.update(byte_array)
print("MD5 digest of the input:")
print(md5.hexdigest())
print(base64.b64encode(md5.digest()))

# SHA256
SHA256 = hashlib.sha256()
SHA256.update(byte_array)
print("SHA256 digest of the input:")
print(SHA256.hexdigest())
print(base64.b64encode(SHA256.digest()))
```

