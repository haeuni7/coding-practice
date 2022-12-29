
n = int(input())

for i in range(n):
    num, string = input().split()
    num = int(num)
    new_ = ""
    for w in string:
        new_ += w * num
    print(new_)
        