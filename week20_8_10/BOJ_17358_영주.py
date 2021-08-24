# 17358. 복불복으로 지구 멸망 (실버5)

N = int(input())
answer = N - 1
for _ in range(N//2-1):
    N -= 2
    answer *= (N - 1)
print(answer % (int(1e9)+7))