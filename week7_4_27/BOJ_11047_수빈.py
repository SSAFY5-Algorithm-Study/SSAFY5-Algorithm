'''
11047. 동전 0

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''
N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
coins.reverse()
cnt = 0

for coin in coins:
    while K >= coin:
        K -= coin
        cnt += 1

print(cnt)
'''
[입력]
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

[출력]
6
'''