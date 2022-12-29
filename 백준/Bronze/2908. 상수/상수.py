def rev(n):
    n = int(n[::-1])
    return n

x,y = input().split()

if rev(x) > rev(y):
    print(rev(x))
else:
    print(rev(y))
           