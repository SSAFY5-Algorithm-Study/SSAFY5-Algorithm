def solution(n, cores):
    # FIFO
    # 이진탐색...?
    s,e = 0, 50000 * 10001
    n -= len(cores)
    # 작업 개수가 코어의 개수보다 작으면?
    # 한 코어당 하나씩 처리해버리면 됨.
    if n < 0:
        for index in range(len(cores)-1,-1,-1):
            n += 1
            if n == 0:
                return index
    else:
        middle = (s+e) // 2
        while True:
            middle = (s+e) // 2
            # 현재 시간까지 처리한 양
            k = 0
            for core in cores:
                k += middle // core
            if k > n:
                if e > s + 1:
                    e = middle
                else:
                    for i in range(len(cores)-1,-1,-1):
                        if not middle % cores[i]:
                            k -= 1
                            if k == n:
                                return i + 1
            elif k < n:
                if e > s + 1:
                    s = middle
                else:
                    for i in range(len(cores)):
                        if not (middle + 1) % cores[i]:
                            k += 1
                            if k == n:
                                return i+1
            else:
                for i in range(len(cores)-1, -1, -1):
                    if not middle%cores[i]:
                        return i+1