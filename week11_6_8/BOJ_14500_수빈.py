'''
14500. 테트로미노

폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 재귀함수로 가능한 사각형
def dfs(x, y, now, cnt):
    global max_sum
    
    # 정사각형이 4개가 되면 최대값과 비교하고 dfs 종료
    if cnt == 4:
        if now > max_sum:
            max_sum = now
        return

    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if not check[nr][nc]:
                check[nr][nc] = 1
                dfs(nr, nc, now+paper[nr][nc], cnt+1)
                check[nr][nc] = 0

# 재귀함수로 못 하는 사각형 어떻게 처리...? T모양,,


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
max_sum = 0


for i in range(N):
    for j in range(M):
        check[i][j] = 1
        dfs(i, j, paper[i][j], 1)
        check[i][j] = 0

print(max_sum)
'''
[입력]
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

[출력]
19
'''