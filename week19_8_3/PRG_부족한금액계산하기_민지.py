"""
price = 3
money = 20
count = 4
------------
total_price -->
첫번째: 3 * 1
두번째: 3 * 2
세번째: 3 * 3
네번째: 3 * 4
+-----------
total_price = 3 * (1+2+3+4) = price * (1+2...+count)
                            = price * ((1+count) * count / 2)

1...N까지를 다 더하는 공식:
(1+N) * N / 2
ex ) 1 ~ 10까지를 더하기 (1+10) * 10 / 2 = 11 * 5 = 55

------------
balance = money - total_price
        = money - (price * ((1+count) * count / 2))
------------
부족한 금액 = -balance -3 --> 3
부족한 금액이 음수라면, 부족한 금액이 없는 것
부족한 금액이 양수일때만 답으로 채택해야함
그러므로 max (0, 부족한 금액)을 해주면 답을 구할 수 있다
"""
def solution(price, money, count):
    return max(0, -(money - (price * ((1+count) * count / 2))))