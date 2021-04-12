# import itertools

# def solution(nums):
#     N = len(nums)
#     case = list(itertools.permutations(nums, N//2))
#     distinct = [list(map(set, c)) for c in case]
#     print(distinct)
#     print(case)
#     max_num = 0
#     for monster in case:
#         length = len(set(monster))
#         if length > max_num:
#             max_num = length
#     # answer = 0
#     return max_num

# nums = [3, 1, 2, 3]
# print(solution(nums))

def solution(nums):
    distinct = len(set(nums))
    answer = min(distinct, len(nums)//2)
    return answer