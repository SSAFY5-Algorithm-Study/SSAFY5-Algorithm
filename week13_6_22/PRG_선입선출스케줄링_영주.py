# Level 4 : 선입 선출 스케줄링
# 정확도만 다 맞고, 효율성은 다 틀림
# parametric search로 풀어야 한다는데, 이해가 잘 안됨

def solution(n, cores):
    length = len(cores)
    counts = [0] * length
    
    while True:
        for i in range(length):
            if counts[i] == 0:
                counts[i] = 1
                n -= 1
                if n == 0:
                    return i + 1
            else:
                counts[i] += 1
            
        for i in range(length):
            if counts[i] == cores[i]:
                counts[i] = 0