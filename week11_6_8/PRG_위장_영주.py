# 해시 : 위장

from collections import Counter

def solution(clothes):
    type_counts = Counter(list(zip(*clothes))[1])
    answer = 1
    for count in type_counts.values():
        answer *= (count+1)
    return answer-1
