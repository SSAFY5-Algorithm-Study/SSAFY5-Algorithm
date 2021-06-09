# 각각 선택하는 경우의 수 : 의상 종류 + 1 (입지 않는 경우 더해주기)
# 경우의 수를 곱해주면 됨.
# 모두 선택을 안하는 경우를 빼면됨

def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 2
    for cloth_kind in clothes_dict.values():
        answer *= cloth_kind
    answer -= 1
    return answer