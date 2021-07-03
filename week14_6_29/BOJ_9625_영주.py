# 9625. BABBA (브론즈1)

# DP
k = int(input())
memo = [0, 1]
for i in range(1, k):
    memo.append(memo[i-1] + memo[i])
print(memo[-2], memo[-1])


"""
# 수학
k = int(input())
A, B = 1, 0
for _ in range(k):
    A, B = B, A
    B += A
print(A, B)
"""