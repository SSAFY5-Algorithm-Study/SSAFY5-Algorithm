def solution(numbers, target):
    # 접근 : 재귀함수를 두개 돌려서, 해당 인덱스의 숫자가 +인 경우와 -인 경우를 모두 고려하기.
    # 수업시간에 배운 내용 활용
    def DFS(level, numbers):
        # 종료조건
        if level >= len(numbers):
            total = sum(numbers)
            # 배열의 합계가 target과 같으면 answer + 1 해주기
            if total == target:
                nonlocal answer
                answer += 1
            return
        DFS(level+1, numbers)
        # - 고려.
        numbers[level] *= (-1)
        DFS(level+1, numbers)
    
    # 11111
    # 1111-1
    # 111-1-1
    # 111-11
    # 11-1-11
    answer = 0
    DFS(0,numbers)
    return answer


# 미친 풀이
def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target+numbers[0]) + solution(numbers[1:], target-numbers[0])