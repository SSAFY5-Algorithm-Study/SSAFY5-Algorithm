# 2개월간의 누적 금액을 기준으로 등급을 정한다.
# 최대 누적 금액을 구해야하므로 최대 누적 금액을 가질 수 있게 해주면 됨
# 첫째 달, 둘째 달을 이용하는 것이므로 첫째 달에서 최대한 많이 가져가게 하면 된다.


def get_values():
    result = 0
    previous_month = 0
    for i in range(len(values)):
        # 해당 등급을 받을 수 있는 최대 금액
        max_value = helper.get(values[i])
        # 첫 번째 달이거나 D등급이면
        if i == 0 or values[i] == 'D':
            # 이번 달 금액 == 등급내에서 가능한 최대 금액
            current_month = max_value
        else:
            # 이번 달 금액 == 등급내에서 가능한 최대 금액 - 이전 달 금액
            current_month = max_value - previous_month
        result += current_month
        # 최대 금액을 이전 달 금액으로 저장
        previous_month = current_month

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