'''
아이디어
-> 헤드기어, 아이웨어, 페이스 별로 나눈다.
-> commbinations 함수를 통해 조합을 만들고
-> 각자 곱해준다.
-> 곱해준 값 + clothes 길이의 값
'''
from itertools import combinations


def solution(clothes):
    answer = len(clothes)

    print(list(combinations([['a', 'd'], 'b'], 1)))
    print(list(combinations([['a', 'd'], 'b'], 2)))
    # clothes_detail = {}
    # # 옷 취합
    # for clothe in clothes:
    #     name, kind = clothe
    #     if clothes_detail.get(kind):
    #         clothes_detail[kind] += 1
    #     else:
    #         clothes_detail[kind] = 1
    # # 옷 종류가 2가지 이상일 때만
    # if len(clothes_detail) > 1:
    #     # 조합값
    #     comb = 1
    #     for value in clothes_detail.values():
    #         comb *= value
    #     answer += comb
    return answer