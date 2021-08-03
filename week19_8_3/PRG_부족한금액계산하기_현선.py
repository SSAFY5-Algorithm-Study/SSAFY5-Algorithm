def solution(price, money, count):
    answer = (sum([i * price for i in range(1, count+1)])) - money
    return answer if answer > 0 else 0