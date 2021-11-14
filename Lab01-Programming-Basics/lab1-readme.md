# readme

## 倪浚桐

## 202022161224

## Lab1

## macOS Big Sur 11.5.2(20G95)

## Pycharm 11.0.11 x86-64

## Python 3.9.5

<img src="/Users/lingfeng/Library/Application Support/typora-user-images/截屏2021-09-24 上午11.36.15.png" alt="截屏2021-09-24 上午11.36.15" style="zoom:50%;" />

```mermaid
graph LR
	hex_srting:str --> |bytes.fromhex|byte_array:bytes
	hex_srting:str --> |is the hex representation of|byte_array:bytes
	byte_array:bytes --> decimal_integers:int
	byte_array:bytes --> |hex|hexadecimal_integers:int
	byte_array:bytes --> |encode:base64|Base64_str:bytes 		
	byte_array:bytes-->|decode:utf-8|text_str:str
	Base64_str:bytes --> |is the base64 representation of|byte_array:bytes
	byte_array:bytes --> |is the utf-8 representation of|text_str:str
	text_str:str --> |deadbeef|hex_srting:str
```

```python
byte_array = bytes.fromhex(hex_string)
```

```python
def bytes_to_dec(in_bytes: bytes) -> None:
    print("decimal integers:", end=' ')
    for b in in_bytes:
        print(b, end=' ')
    print()
```

```python
def bytes_to_hex(in_bytes: bytes) -> None:
    print("hexadecimal integers:", end=' ')
    for b in in_bytes:
        print(hex(b), end=' ')
    print()
```

```python
def encode_base64(in_bytes: bytes) -> None:
    print("Base64_str:", end=' ')
    print(base64.b64encode(in_bytes))
```

```python
def decode_utf8(in_bytes: bytes) -> str:
    print("text_str:", end=' ')
    return in_bytes.decode('utf-8')
```



