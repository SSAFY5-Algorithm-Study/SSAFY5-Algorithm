'''
https://programmers.co.kr/learn/courses/30/lessons/42578
'''
def solution(clothes):
    total = 1
    spy = {}
    
    for cloth in clothes:
        name, kind = cloth
        # 각 의상을 입지 않은 경우도 포함시켜주려고 초기 값 1
        # 0으로 하고 다 곱하면 상의, 하의, 모자가 있을 때 상의, 하의만 입은 경우 포함하지 않음
        spy[kind] = spy.get(kind, 1) + 1
        
    for i in list(spy.values()):
        total *= i
        
    # 조건에서 하루에 최소 한 개의 의상은 입는다고 했으므로 다 입지 않은 경우 빼줌
    return total - 1