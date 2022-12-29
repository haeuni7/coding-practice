def hansu(num) :
    cnt = 0
    for i in range(1, num+1):
        nlst = list(map(int,str(i)))
        if i < 100:
            cnt += 1  # 100보다 작으면 한수인듯(공차가 2개 미만이라?)
        elif nlst[0]-nlst[1] == nlst[1]-nlst[2]:
            cnt += 1 
    return cnt

num = int(input())
print(hansu(num))