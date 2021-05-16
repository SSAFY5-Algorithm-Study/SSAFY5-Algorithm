def solution(numbers, target):
    answer = [0]
    def DFS(level, total):
        if level >= len(numbers):
            if total == target:
                answer[0] += 1
            return
        DFS(level + 1, total + numbers[level])
        DFS(level + 1, total - numbers[level])
    DFS(0, 0)

    return answer[0]