"""
dp 배열의 의미
dp[N]은 N번째 칸에서 시작하는 단어까지 포함했을때 현재 위치에서 몇개의 pPAp를 만들 수 있는지 저장하는 배열

예제
ApPApPpAPpApPAp
dp[0] = 0 --> ApPA != pPAp
dp[1] = 1 --> pPAp == pPAp
dp[2] = 1 --> PApP != pPAp --> dp[1]에서 가져옴
dp[3] = 1 --> ApPp != pPAp --> dp[2]에서 가져옴
dp[4] = 1
dp[5] = 1
dp[6] = 1
dp[7] = 1
...
dp[11] = 2 --> pPAp == pPAp --> dp[7] + 1

규칙
1. i번째 칸에서 시작하는 단어가 pPAp가 아닌경우
    - dp[i] = dp[i-1]
2. i번째 칸에서 시작하는 단어가 pPAp인 경우
    - dp[i] = max(dp[i-4]+1, dp[i-1])
    - 현재칸에서 시작을 한다면 현재칸 기준 3칸 전까지는 pPAp를 시작하면 안된다 (겹치는 글자가 생기기때문)
    - 현재칸 기준으로 4칸전까지의 글자는 사용가능
    - 그러므로 dp[i-4] + 1 또는 dp[i-1]중 더 큰 경우의 수를 고른다
"""
def cnt_ppap(N, letters):
    cnt = 0
    dp = [0] * (N-3)

    if N <= 3:
        return 0
    for i in range(0, N-3):
        if letters[i:i+4] == 'pPAp':
            dp[i] = max(dp[i-4]+1, dp[i-1])
        else:
            dp[i] = dp[i-1]
    return max(dp[-4:])

N = int(input())
letters = input()
print(cnt_ppap(N, letters))


