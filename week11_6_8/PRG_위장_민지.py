from math import prod

def solution(clothes):
    clothes_count = {}
    for name, cat in clothes:
        clothes_count[cat] = clothes_count.get(cat, 1) + 1
    
    answer = prod(clothes_count.values()) - 1
    return answer