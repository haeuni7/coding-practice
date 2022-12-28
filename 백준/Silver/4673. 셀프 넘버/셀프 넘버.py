
def d(n):
    fir = n//10000
    sec = (n%10000)//1000
    thi = (n%10000%1000)//100
    fou = (n%10000%1000%100)//10
    fif = n%10000%1000%100%10
    ans = n + fir + sec + thi + fou + fif
    
    return ans

lst = [i for i in range(1, 10001)]
dlst = [d(i) for i in range(1, 10001)]

for i in lst:
    if i not in dlst:
        print(i)