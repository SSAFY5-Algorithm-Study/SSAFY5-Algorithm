import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 최솟값을 만들어야 해서 오름차순 정렬 진행
    cards = sorted(list(map(int, input().split())))
    idx = 0
    for _ in range(M):
        number = cards[idx] + cards[idx + 1]
        cards[idx], cards[idx + 1] = number
        if number > cards[idx + 2]:
            idx += 1

