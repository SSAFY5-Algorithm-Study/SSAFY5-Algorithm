def solution(word):
    vowel_dict = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    answer = 0
    multiplier = 781
    
    for i in range(len(word)):
        answer += multiplier * vowel_dict.get(word[i]) + 1
        multiplier //= 5
    
    return answer