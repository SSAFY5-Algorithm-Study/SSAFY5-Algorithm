"""
N = 교차로의 총 갯수
AM = 교차로 간의 연결 관계를 표현할 adjacent matrix
m = 각 교차로와 연결된 교차로 갯수 (첫번째 줄)
c (connected) = 연결된 교차로의 번호 리스트 (두번째 줄)
"""
def is_cycle(AM):
    for i in range(1, N):
        for j in range(i+1, N+1):
            if AM[i][j] and AM[j][i]:
                return "CYCLE"
    return "NO CYCLE"


N = int(input())
AM = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N):
    m = int(input())
    c = list(map(int, input().split()))
    for j in c:
        # AM[1][2] == 1 이라면, 1 --> 2로 가는 길이 연결돼있음
        AM[i][j] = 1 

print(is_cycle(AM))
