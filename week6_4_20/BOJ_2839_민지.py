N = int(input())

cnt = 0
while N >= 0:
    if N % 5 == 0:
        cnt += N//5
        break
    cnt += 1
    N -= 3
else:
    cnt = -1
print(cnt)