# from itertools import combinations

# n, c = map(int, input().split())
# axis = [int(input()) for _ in range(n)]

# axis.sort()
# axis_combs = list(combinations(axis, c))
# max_value = -987654321
# for comb in axis_combs:
#     min_value = 987654321
#     for i in range(c - 1):
#         min_value = min(min_value, comb[i+1] - comb[i])
#         if min_value < max_value:
#             break
#     max_value = max(min_value, max_value)

# print(max_value)


n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]

houses.sort()
start = 1
end = houses[-1] - houses[0]
answer = []

while start <= end:
    count = 1
    pivot = houses[0]
    mid = (start + end) // 2
    for i in range(1, n):
        if pivot + mid <= houses[i]:
            count += 1
            pivot = houses[i]
    if count >= c:
        start = mid + 1
        answer.append(mid)
    else:
        end = mid - 1
print(max(answer))