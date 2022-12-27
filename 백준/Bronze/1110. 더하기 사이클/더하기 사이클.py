import sys
input = sys.stdin.readline

n = int(input())
org = n
cnt = 0

while 1:
    left = n//10
    right = n%10
    a = str(left+right)
    n = int(str(right)+a[-1])
    cnt += 1
    if n == org:
        print(cnt)
        break
    elif n != org:
        continue
        