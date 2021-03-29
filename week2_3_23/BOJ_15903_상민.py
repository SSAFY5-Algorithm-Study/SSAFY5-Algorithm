import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 최솟값을 만들어야 해서 오름차순 정렬 진행
    cards = sorted(list(map(int, input().split())))
    # M만큼 수행
    for _ in range(M):
        # 오름차순 정렬된 `cards`에서 첫 번째와 두 번째를 더해주고
        sum_value = cards[0] + cards[1]
        # 값을 더한 값으로 바꿔준다.
        cards[0] = cards[1] = sum_value
        # 오름 차순 정렬
        cards = sorted(cards)
    # 카드 숫자들 합계 출력
    print(sum(cards))