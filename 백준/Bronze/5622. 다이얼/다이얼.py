a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
n = list(input())

time = 0
for i in n:
    for j in a:
        if i in j:
            time += a.index(j)+3
    # 원래 수에서 1씩 더해주면 소요시간
print(time)