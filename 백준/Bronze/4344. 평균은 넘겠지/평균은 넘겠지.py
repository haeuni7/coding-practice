import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    lst = list(map(int, input().split()))
    num = lst[0]
    m = sum(lst[1:])/num
    cnt = 0
    for i in lst[1:]:
        if i > m:
            cnt += 1
    print(f"{cnt/num*100:.3f}%")