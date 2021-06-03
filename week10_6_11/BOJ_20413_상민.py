# 2개월간의 누적 금액을 기준으로 등급을 정한다.
# 최대 누적 금액을 구해야하므로 최대 누적 금액을 가질 수 있게 가정해주면 됨
# 첫째 달, 둘째 달을 이용하는 것이므로 첫째 달에서 최대한 많이 가져가게 하면 된다.

# BSG
# B등급이면, 29까지니,
# 첫째 달 = 29
# S등급이면, 59까지니,
# 59 - 첫째 달 = 30
# G등급이면, 89까지니,
# 89 - 둘째 달 = 59

# 29 + 30 + 59 = 118

# 그렇다면, 주어진 등급 기준 - 1만큼까지 가능한 상황에서
# 첫째 달은 그 자체가 답이 됨
# 둘째 달 부터는 가능한 최대치 - 그 전 달을 해주면 됨


def get_values():
    result = 0
    previous = 0
    for i in range(len(values)):
        # 최대값 - 1
        max_value = helper.get(values[i])
        # 첫 번째 달이면
        if i == 0:
            # 최댓값 더해주고
            result += max_value
            # 저장
            previous = max_value
        elif values[i] == 'D':
            previous = max_value
            result += max_value
        else:
            previous = max_value - previous
            result += previous
    return result


N = int(input())
s, g, p, d = map(int, input().split())
values = input()
helper = {
    'B': s - 1,
    'S': g - 1,
    'G': p - 1,
    'P': d - 1,
    'D': d,
}

print(get_values())