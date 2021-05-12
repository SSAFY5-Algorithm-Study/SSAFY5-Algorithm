'''
1248. 맞춰봐

https://www.acmicpc.net/problem/1248
'''
# 체크 필요한 경우
def check(idx):
    s = 0
    for i in range(idx, N):
        s += ans[i]
        if s == 0 and S[idx][i] != '0':
            return False
        if s > 0 and S[idx][i] != '+':
            return False
        if s < 0 and S[idx][i] != '-':
            return False
    return True

def get_ans(idx):

    if idx == -1:
        return True
    
    if S[idx][idx] == '0':
        ans[idx] = 0
        return get_ans(idx-1)
    
    for i in range(-10, 11):
        ans[idx] = i
        if check(idx) and get_ans(idx-1):
            return True
    
    return False


N = int(input())
sign = list(input())

# 행렬로 표현하기
S = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        S[i][j] = sign.pop(0)

ans = [0] * N
get_ans(N-1)
print(*ans)

'''
[입력]
4
-+0++++--+

[출력]
-2 5 -3 1
'''