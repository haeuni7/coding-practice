import sys
input = sys.stdin.readline


a,b,c = map(int, input().split())
# 세 수가 같은 경우
if a==b==c:
    print(10000 + 1000*a)
# 두 수가 같은 경우
elif a==b or a==c:
    print(1000 + 100*a)
elif b==c:
    print(1000 + 100*b)
# 모두 다른 경우
elif a!=b!=c:
    p = sorted([a,b,c])
    print(p[-1]*100)
        
        