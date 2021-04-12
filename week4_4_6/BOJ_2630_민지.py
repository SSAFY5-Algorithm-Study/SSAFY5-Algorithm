import sys
sys.stdin = open('input.txt', 'r')


def cnt_square(sr, er, sc, ec):
    global blue_cnt, white_cnt

    color = square[sr][sc]
    for r in range(sr, er):
        for c in range(sc, ec):
            if square[r][c] != color:
                # 쪼개기
                cnt_square(sr, (sr+er)//2, sc, (sc+ec)//2)
                cnt_square(sr, (sr+er)//2, (sc+ec)//2, ec)
                cnt_square((sr+er)//2, er, sc, (sc+ec)//2)
                cnt_square((sr+er)//2, er, (sc+ec)//2, ec)
                return
    else:
        if color:
            blue_cnt += 1
        else:
            white_cnt += 1

N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]
blue_cnt = 0
white_cnt = 0
cnt_square(0, N, 0, N)
print(white_cnt)
print(blue_cnt)
