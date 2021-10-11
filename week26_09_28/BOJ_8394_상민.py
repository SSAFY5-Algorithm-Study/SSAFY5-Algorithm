N = int(input())
DP = [0 for _ in range(N + 1)]
DP[1] = 1
DP[2] = 2
for i in range(3, N + 1):
    # 첫 째 자리 수만 구하면 되기 때문에 10으로 나눈 나머지만 DP 배열에 저장
    # 만약에, 안해주면 메모리 초과남...:(
    DP[i] = (DP[i-1] + DP[i-2]) % 10

print(DP[-1])