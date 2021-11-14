# readme

## 倪浚桐

## 202022161224

## Lab2-progarm2

## macOS Big Sur 11.5.2(20G95)

## Pycharm 11.0.11 x86-64

## Python 3.9.5

<img src="/Users/lingfeng/Desktop/截屏2021-09-28 下午9.28.11.png" alt="截屏2021-09-28 下午9.28.11" style="zoom:50%;" />

```python
#!/usr/bin/env python3 

n = input("please input n:")
keyword = input("please input keyword:")
plaintext = input("please input plaintext:")
cnt = int(n)
pos = 1
ans = ""
keyword = keyword.replace(' ', '')
while cnt:
    for i in keyword:
        if i == str(pos):
            index = keyword.find(i)
            for x in plaintext[int(index)::int(n)]:
                ans += x
            cnt -= 1
            pos += 1
            break
print("ciphertext:", end=" ")
print(ans)
```

