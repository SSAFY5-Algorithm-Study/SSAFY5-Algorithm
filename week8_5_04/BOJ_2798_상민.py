def pick_card(idx, num, card_sum):
    if card_sum > M:
        return
    if num >= 3:
        max_value[0] = max(card_sum, max_value[0])
        return

    if idx >= N:
        return

    pick_card(idx + 1, num + 1, cards[idx] + card_sum)
    pick_card(idx + 1, num, card_sum)

N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_value = [0]
pick_card(0, 0, 0)
print(max_value[0])