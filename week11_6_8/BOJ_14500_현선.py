'''
문제
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.



아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 
종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다.
 i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 
 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
'''
# 모르겠다.....걍 다해보자........후.....
# 무지성 코딩. 거의 침팬치나 원숭이급

n,m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
total_max = 0

# 정사각형
for i in range(n-1):
    for j in range(m-1):
        temp = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1]
        if total_max < temp:
            total_max = temp

# 일자 긴거 가로
for i in range(n):
    for j in range(m-3):
        temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3]
        if total_max < temp:
            total_max = temp

# 일자 긴거 세로
for i in range(n-3):
    for j in range(m):
        temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j]
        if total_max < temp:
            total_max = temp

# L자 
for i in range(n-2):
    for j in range(m-1):
        temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]
        if total_max < temp:
            total_max = temp

# L자 대칭
for i in range(n-2):
    for j in range(1,m):
        temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j-1]
        if total_max < temp:
            total_max = temp

# ㄱ자
for i in range(n-1):
    for j in range(m-2):
        temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2]
        if total_max < temp:
            total_max = temp

# ㄱ자 대칭
for i in range(n-1):
    for j in range(m-2):
        temp = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i][j+2]
        if total_max < temp:
            total_max = temp

# # ㄱ자 위에 짧은거
for i in range(n-2):
    for j in range(m-1):
        temp = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1]
        if total_max < temp:
            total_max = temp

# ㄱ자 위에 짧은거 대칭
for i in range(n-2):
    for j in range(m-1):
        temp = paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+2][j]
        if total_max < temp:
            total_max = temp

# ㄴ자
for i in range(n-1):
    for j in range(m-2):
        temp = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
        if total_max < temp:
            total_max = temp

# ㄴ자 대칭
for i in range(1,n):
    for j in range(m-2):
        temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i-1][j+2]
        if total_max < temp:
            total_max = temp
# ㅜ자
for i in range(n-1):
    for j in range(m-2):
        temp = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i][j+2]
        if total_max < temp:
            total_max = temp

# ㅗ자
for i in range(1,n):
    for j in range(m-2):
        temp = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i][j+2]
        if total_max < temp:
            total_max = temp

# ㅓ자. 다시 확인?
for i in range(1, n-1):
    for j in range(m-1):
        temp = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i+1][j+1]
        if total_max < temp:
            total_max = temp
# print(total_max)

# ㅏ자
for i in range(n-2):
    for j in range(m-1):
        temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1]
        if total_max < temp:
            total_max = temp

# 이상한 모양
for i in range(n-2):
    for j in range(m-1):
        temp = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]
        if total_max < temp:
            total_max = temp

# 이상한 모양 90도 회전
for i in range(1, n):
    for j in range(m-2):
        temp = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i-1][j+2]
        if total_max < temp:
            total_max = temp

# 이상한 모양 반전
for i in range(n-2):
    for j in range(1,m):
        temp = paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+2][j-1]
        if total_max < temp:
            total_max = temp

# 이상한 모양 90도 회전의 반전
for i in range(n-1):
    for j in range(m-2):
        temp = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2]
        if total_max < temp:
            total_max = temp

print(total_max)