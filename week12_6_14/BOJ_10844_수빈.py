'''
10844. 쉬운 계단 수

45656이란 수를 보자.
이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)
'''
BASE = 10 ** 9
N = int(input())

stairs = [[0 for _ in range(10)] for _ in range(N+1)]
stairs[1] = [0] + [1] * 9

for i in range(2, N+1):
    for j in range(10):
        # 오른쪽 위 대각선
        if j == 0:
            # stairs[i][j] = stairs[i-1][j+1]
            stairs[i][j] = stairs[i-1][1]
        # 왼쪽 위 대각선
        elif j == 9:
            # stairs[i][j] = stairs[i-1][j-1]
            stairs[i][j] = stairs[i-1][8]
        # 양쪽 위 대각선
        else:
            stairs[i][j] = stairs[i-1][j-1] + stairs[i-1][j+1]

print(sum(stairs[N]) % BASE)
'''
[입력]
1

[출력]
9
'''