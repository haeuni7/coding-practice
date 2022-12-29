# 소문자로 변환, 알파벳 개수 세기, 대문자 or "?" 출력
# 문자열 길이가 1000,000 이하라서 for문 쓰면 시간초과인듯. -> 정답보고 set함수씀
w = input().upper()
u = list(set(w))
ans = {}

# 알파벳:빈도수 로 구성된 딕셔너리
for i in u:
    ans[i] = w.count(i)
    
ans = sorted(ans.items(), key = lambda x:x[1])

if len(u) > 1:
    if ans[-1][1] != ans[-2][1]:
        print(ans[-1][0])
    else:
        print("?")
else: # 문자열이 한 글자인 경우
    print(ans[-1][0])

