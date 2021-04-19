import sys
sys.stdin = open('input.txt')


stick_length = (64, 32, 16, 8, 4, 2, 1)

T = int(input())
for tc in range(1, T + 1):
    X = int(input())
    answer = 0
    for length in stick_length:
        if X >= length:
            X -= length
            answer += 1
        if X == 0:
            break
    print(answer)

