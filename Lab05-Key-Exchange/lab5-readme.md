# readme

## 倪浚桐

## 202022161224

## Lab5

## macOS Monterey 12.0.1

## Pycharm 11.0.12 x86-64

## Python 3.9.5

![Screen Shot 2021-11-07 at 10.05.51 AM](/Users/lingfeng/Desktop/Screen Shot 2021-11-07 at 10.05.51 AM.png)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# 快速幂模运算，把b拆分为二进制，遍历b的二进制，当二进制位为0时不计入计算
def quick_pow_mod(a: int, b: int, c: int) -> int:
    a = a % c
    ans: int = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a % c) * (a % c)
    return ans


if __name__ == '__main__':
    p = 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627
    g = 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729
    a = random.randint(1, 156)  # syntax reference: https://docs.python.org/3/library/random.html
    b = random.randint(1, 156)
    A = quick_pow_mod(g, a, p)  # syntax reference: https://www.geeksforgeeks.org/pow-in-python/
    B = quick_pow_mod(g, b, p)
    Ka = quick_pow_mod(B, a, p)
    Kb = quick_pow_mod(A, b, p)
    print("Alice to Bob:")
    print(str(A))
    print("Bob to Alice:")
    print(str(B))
    print("Result (Alice view):")
    print(str(Ka))
    print("Result (Bob view):")
    print(str(Kb))
```

