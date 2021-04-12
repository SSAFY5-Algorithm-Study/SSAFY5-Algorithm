'''
2630. 색종이 만들기

https://www.acmicpc.net/problem/2630
'''
# 계속 절반씩 잘라가면서 모두 같은 색이 되는 경우 count
# 분할 - 정복

def check_color(r, c, size):
    global blue, white
    # 기준점의 색깔
    base = paper[r][c]
    for i in range(r, r + size):
        for j in range(c, c + size):
            # 기준점의 색깔과 다른 색이 나온다면
            if base != paper[i][j]:
                # 4등분해서 다시 탐색
                check_color(r, c, size//2)
                check_color(r, c + size//2, size//2)
                check_color(r + size//2, c, size//2)
                check_color(r + size//2, c + size//2, size//2)
                return
    
    if base == '0':
        white += 1
        return
    else:
        blue += 1
        return

# 전체 종이의 크기
N = int(input())
# 색종이 상태 배열
paper = [list(input().split()) for _ in range(N)]
# 색종이의 개수 저장할 변수
white = 0
blue =  0
check_color(0, 0, N)

print(white)
print(blue)
'''
[입력]
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

[출력]
9
7
'''