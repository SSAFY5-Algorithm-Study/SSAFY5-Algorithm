'''
i번째 포도주를 마시고 i-2번째까지 마신 양,
i,i-1번째를 포도주를 마시고 i-3번째까지 마신 양,
그리고 i번째를 마시지 않는 경우(i-1번째 포도주까지 마신 양)를 모두 고려해야한다.
'''

n = int(input())
d = [0] * 10001
wine = [int(input()) for _ in range(n)]
if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[1] + wine[0])
else:
    d[0] = wine[0]
    d[1] = wine[0] + wine[1]
    d[2] = max(wine[0] + wine[2], wine[1] + wine[2], d[1])
    for i in range(3, n):
        d[i] = max(d[i-2] + wine[i], wine[i-1] + wine[i] + d[i-3], d[i-1])
    print(max(d))