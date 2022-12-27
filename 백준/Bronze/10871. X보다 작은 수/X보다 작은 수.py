import sys
input = sys.stdin.readline

num, key = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []

for i in lst:
    if i >= key:
        pass
    elif i < key:
        nlst.append(i)
for i in nlst:
    print(i, sep=" ")
     
    