# DFS/BFS 타겟넘버

def solution(numbers, target):
    length = len(numbers)

    def dfs(total, depth):
        if depth >= length:
            return 1 if total == target else 0
        return total + dfs(total+numbers[depth], depth+1) + dfs(total-numbers[depth], depth+1)

    return dfs(0, 0)
