import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

tri = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

def find_max_path(r, c, t_sum):
    global max_sum 
    if r == N:
        if t_sum > max_sum:
            print(r, c, t_sum)
            max_sum = t_sum
            return
    
    elif 0 <= c < N:
        t_sum += tri[r][c]
        find_max_path(r+1, c, t_sum)
        find_max_path(r+1, c+1, t_sum)

find_max_path(0, 0, 0)

for i in range(1, N):
    