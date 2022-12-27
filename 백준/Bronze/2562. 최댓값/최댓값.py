import sys
input = sys.stdin.readlines

lst = list(map(int, input()))
m = max(lst)
print(m)

for i in range(len(lst)):
    if lst[i] == m:
        print(i+1)

