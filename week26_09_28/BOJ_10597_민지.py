from itertools import permutations

num = input()

if len(num) <= 9:
    for i in num:
        print(i, end=' ')
else:
    N = (len(num) - 9) // 2 + 9
    print(list(permutations(range(1, N+1))))