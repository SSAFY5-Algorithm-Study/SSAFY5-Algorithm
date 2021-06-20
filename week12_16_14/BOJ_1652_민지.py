import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
room = [input() for _ in range(N)]

# 방법 1: 함수화 하지 않고 row, col 따로 나눠서 풀기
row_cnt = col_cnt = 0

for i in range(N):
    cnt = 0
    for j in range(0, N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                row_cnt += 1
            cnt = 0
    if cnt >= 2:
        row_cnt += 1

for j in range(N):
    cnt = 0
    for i in range(0, N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                col_cnt += 1
            cnt = 0
    if cnt >= 2:
        col_cnt += 1

print(row_cnt, col_cnt)

# 방법 2: 함수화 해서 row, col을 한번에 처리할 수 있는 함수 만들기
def find_cnt(d):
    direction = {'row': lambda i, j: room[i][j], 'col': lambda i, j: room[j][i]}
    ans = cnt = 0
    for i in range(N):
        for j in range(0, N):
            if direction[d](i, j) == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    ans += 1
                cnt = 0
        if cnt >= 2:
            ans += 1
        cnt = 0
    return ans

print(str(find_cnt('row')) + " " + str(find_cnt('col')))