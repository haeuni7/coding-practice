import sys
input = sys.stdin.readlines

lst = list(map(int, input()))
a = []

for i in lst:
    a.append(i % 42)

a = list(set(a))
print(len(a))