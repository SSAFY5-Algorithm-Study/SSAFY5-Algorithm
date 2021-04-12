def solution(nums):
    unique = len(set(nums))
    answer = min(unique, len(nums)/2)
    return answer