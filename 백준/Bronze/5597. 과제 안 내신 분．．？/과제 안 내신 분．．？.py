import sys 
input = sys.stdin.readlines

lst = sorted(list(map(int, input())))

for i in range(1, 31):
    if i in lst:
        pass
    elif i not in lst:
        print(i)