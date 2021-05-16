from collections import deque

def solution(numbers, target):
    answer = 0
    length = len(numbers)
    # queue = [(numbers[0], 0), (-1*numbers[0], 0)]
    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-1*numbers[0], 0))
    
    while queue:
        temp, level = queue.popleft()
        # 다음 숫자를 더하거나 빼줘야하기 때문에 +1
        level += 1
        if level < length:
            queue.append((temp + numbers[level], level))
            queue.append((temp - numbers[level], level))
        else:
            if temp == target:
                answer += 1
    return answer