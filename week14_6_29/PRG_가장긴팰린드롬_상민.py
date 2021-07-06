# 기존 코드 (38점)
# def solution(s):
#     answer = 0
#     for i in range(len(s)):
#         start, end = i, len(s) - 1
#         temp = 0
#         while end >= start:
#             if s[start] == s[end]:
#                 if start == end:
#                     temp += 1
#                     break
#                 start += 1
#                 end -= 1
#                 temp += 2
#             else:
#                 if temp:
#                     temp = 0
#                     break
#                 end -= 1
#         answer = max(temp, answer)
#         if answer == len(s):
#             return answer
#     return answer


# 풀이 코드


def solution(s):
    answer = 0
    for i in range(len(s)):
        start, end = i, len(s)
        while end > start:
            word = s[start:end]
            if word == word[::-1]:
                answer = max(answer, len(word))
            end -= 1
    return answer
