s = '严'
s.encode('utf-8')
print(type(s), s)

s.encode('utf-8').decode('utf-8')
print(type(s), s)