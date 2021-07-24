# 73점


def rotate(key):
    m = len(key)
    A = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            A[j][m-i-1] = key[i][j]
    return A

def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    arr = [[0] * (2*(m-1)+n) for i in range(2 * (m-1)+n)]
    N = 0
    C = 0
    for i in range(n):
        for j in range(n):
            arr[m-1+i][m-1+j] = lock[i][j]
            if lock[i][j] == 0:
                N += 1
    for _ in range(4):
        if answer:
            break
        key = rotate(key)
        x = 0
        y = 0
        while x <= m+n-2 and y <= m+n-2:
            for i in range(m):
                if C < 0:
                    break   
                for j in range(m):
                    if m-1 <= x+i <= m+n-2 and m-1 <= y+j <= m+n-2:
                        if arr[x+i][y+j] == 0 and key[i][j] == 1:
                            C += 1
                        else:
                            if arr[x+i][y+j] == 1 and key[i][j] == 1:
                                C = -1
                                break
                if N == C:
                    answer = True
                    break
                else:
                    C = 0
                    if x < m+n-2:
                        x += 1
                    else:
                        y += 1
                        x = 0
    return answer