from itertools import permutations

n = int(input())
nums = [i for i in range(1, n+1)]
result = sorted(list(permutations(nums,n)))
# print(result)

arr = list(map(int,input().split()))
if arr[0] == 1:
    num = arr[1]
    print(*result[num-1])
else:
    per = tuple(arr[1:])
    for i in range(len(result)):
        if per == result[i]:
            print(i+1)

