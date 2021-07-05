# Level 3 : 가장 긴 팰린드롬

def solution(s):
    max_length = 1
    for i in range(len(s)):
        end = len(s)
        while max_length < end - i:
            word = s[i:end]
            if word == word[::-1]:
                max_length = end - i
            end -= 1
    return max_length
