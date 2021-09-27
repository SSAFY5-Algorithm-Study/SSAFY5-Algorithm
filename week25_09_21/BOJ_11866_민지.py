N, K = map(int, input().split())

idx = -1
nums = list(range(1, N+1))
order = []

while N > 0:
    idx = (idx + K) % N
    if nums[idx] != 0:
        order.append(nums.pop(idx))
        idx -= 1
        N -= 1

print("<" + ", ".join(map(str, order)) + ">")