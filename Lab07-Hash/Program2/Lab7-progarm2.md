# readme

## 倪浚桐

## 202022161224

## Lab7-progarm2

## macOS Monterey 12.0.1

## Pycharm 11.0.12 x86-64

## Python 3.9.5

![Screen Shot 2021-11-30 at 7.47.45 PM](/Users/lingfeng/Desktop/Screen Shot 2021-11-30 at 7.47.45 PM.png)

```python
import hashlib

password_str: str = input()
password_bytes: bytes = bytes(password_str, encoding="utf8")
salt_hex: str = input()
salt_bytes: bytes = bytes.fromhex(salt_hex)

n = 4
r = 8
p = 16
print(hashlib.scrypt(password_bytes, salt=salt_bytes, n=4, r=8, p=16).hex())

# hashlib.scrypt(password, *, salt, n, r, p, maxmem=0, dklen=64)
# 此函数提供基于密码加密的密钥派生函数，其定义参见 RFC 7914。
# password 和 salt 必须为 字节类对象。 应用和库应当将 password 限制在合理长度 (例如 1024)。 salt 应当为适当来源例如 os.urandom() 的大约 16 个或更多的字节串数据。
# n 为 CPU/内存开销因子，r 为块大小，p 为并行化因子，maxmem 为内存限制 (OpenSSL 1.1.0 默认为 32 MiB)。 dklen 为派生密钥的长度。
# ！！！注意python中*的含义！！！
```

