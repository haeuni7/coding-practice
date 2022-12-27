import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    cnt = 0
    score = 0
    a = input()
    for i in a:
        if i == "O":
            cnt += 1
            score += cnt
        elif i == "X":
            cnt = 0
    print(score)
            
    