def is_palindrome(s):
    return s == s[::-1]

def solution(s):
    length = len(s)
    max_length = 0
    
    for i in range(length):
        for j in range(i, length+1):
            if is_palindrome(s[i:j]):
                max_length = max(max_length, len(s[i:j]))
    
    return max_length