import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
nlst = []

for i in lst:
    nlst.append(i/m*100)
print(sum(nlst)/n)