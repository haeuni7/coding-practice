def rev(n):
    nlst = []
    for i in n[::-1]:
        nlst.append(i)
    return int("".join(nlst))

x,y = input().split()

if rev(x) > rev(y):
    print(rev(x))
else:
    print(rev(y))
           