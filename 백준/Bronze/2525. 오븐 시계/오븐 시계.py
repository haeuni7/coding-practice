import sys
input = sys.stdin.readline

h,m = map(int, input().split())
time = int(input())
fin = m+time

if fin >= 60:
    c = fin//60
    h += c
    m = fin - 60*c
    if h < 24:
        print(h, m)
    elif h >= 24:
        c = h//24
        h = h - 24*c
        print(h, m)
    
elif fin < 60:
    m += time
    if h < 24:
        print(h, m)
    elif h >= 24:
        c = h//24
        h = h - 24*c
        print(h, m)
        
