import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    fruits = sorted(list(map(int, input().split())))

    for fruit in fruits:
        if L >= fruit:
            L += 1
    # break문 생각
    print(tc, L)