
# 풀이 참조

def prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def recursive(start, k):
    if k == 0:
        print("%d" % start)
    for i in range(1, 10, 2):
        temp = start * 10 + i
        if prime(temp):
            recursive(temp, k-1)
n = int(input())
sosu = [2, 3, 5, 7]
for i in range(4):
    recursive(sosu[i], n-1)
