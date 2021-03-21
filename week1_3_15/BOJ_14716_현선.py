'''
문제
ANT가 처음 알고리즘 대회를 개최하게 되면서 현수막을 내걸었다.

저번 학기 영상처리 수업을 듣고 배웠던 지식을 최대한 응용 해보고 싶은 혁진이는 이 현수막에서 글자가 몇 개인지 알아보는 프로그램을 만들려 한다.

혁진이는 우선 현수막에서 글자인 부분은 1, 글자가 아닌 부분은 0으로 바꾸는 필터를 적용하여 값을 만드는데 성공했다.

그런데 혁진이는 이 값을 바탕으로 글자인 부분 1이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결되어 있다면 한 개의 글자라고 생각만 하였다.

혁진이가 필터를 적용하여 만든 값이 입력으로 주어졌을 때, 혁진이의 생각대로 프로그램을 구현하면 글자의 개수가 몇 개인지 출력하여라.

입력
첫 번째 줄에는 현수막의 크기인 M와 N가 주어진다. (1 ≤ M, N ≤ 250)

두 번째 줄부터 M+1 번째 줄까지 현수막의 정보가 1과 0으로 주어지며, 1과 0을 제외한 입력은 주어지지 않는다.

출력
혁진이의 생각대로 프로그램을 구현했을 때, 현수막에서 글자의 개수가 몇 개인지 출력하여라.
'''

# 상,하,좌,우,오위,오아,왼위,왼아
# dr = [-1, 1, 0, 0, -1, 1, -1, 1]
# dc = [0, 0, -1, 1, 1, 1, -1, -1]

# 런타임 에러....
# # 재귀. 우째풀지...
# def DFS(r,c):
#     if hyunsoomak[cr][cc] == 0:
#         return
#     visited[r][c] = 1
#     for i in range(8):
#         cr = r + dr[i]
#         cc = c + dc[i]
#         if 0 <= cr < M and 0 <= cc < N and hyunsoomak[cr][cc] and visited[cr][cc] == 0: 
#             visited[cr][cc] = 1
#             DFS(cr,cc)

dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

def DFS(sr,sc):
    visited[sr][sc] = 1
    stack = [[sr,sc]]
    while stack:
        r, c = stack.pop()
        for i in range(8):
            cr = r + dr[i]
            cc = c + dc[i]
            if 0 <= cr < M and 0 <= cc < N and hyunsoomak[cr][cc]: 
                if visited[cr][cc] == 0:
                    visited[cr][cc] = 1
                    stack.append([cr,cc])


M, N = map(int,input().split())
hyunsoomak = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
result = 0
for i in range(M):
    for j in range(N):
        if hyunsoomak[i][j] and visited[i][j] == 0:
            DFS(i,j)
            result += 1
print(result)