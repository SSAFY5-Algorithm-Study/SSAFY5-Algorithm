def solution(price, money, count):
    return max(0, -(money - price * ((count+1)*count)/2))