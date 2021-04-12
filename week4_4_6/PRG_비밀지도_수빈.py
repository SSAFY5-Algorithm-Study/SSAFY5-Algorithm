def solution(n, arr1, arr2):
    map1 = [bin(num)[2:].zfill(n) for num in arr1]
    map2 = [bin(num)[2:].zfill(n) for num in arr2]
    secret = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                secret[i] += ' '
            else:
                secret[i] += '#'
    return secret