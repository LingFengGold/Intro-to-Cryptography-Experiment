#!/usr/bin/env python3 

n: str = input("please input n:")
keyword: str = input("please input keyword:")
plaintext: str = input("please input plaintext:")
cnt: int = int(n)
pos: int = 1
ans: str = ""
keyword: str = keyword.replace(' ', '')
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
