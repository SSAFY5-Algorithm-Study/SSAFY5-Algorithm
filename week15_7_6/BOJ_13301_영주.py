# 13301. 타일 장식물 (브론즈1)

def get_area(n):
    if n <= 1:
        return 4
    memo = [1, 1]
    for _ in range(n-2):
        memo.append(memo[-2]+memo[-1])
    return (memo[-2]*2) + (memo[-1]*4)


print(get_area(int(input())))