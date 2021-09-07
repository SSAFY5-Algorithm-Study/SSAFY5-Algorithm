def solution(word):
    word_dict = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4
    }
    w = [781, 156, 31, 6, 1]
    answer = 0
    answer += len(word)
    for i in range(len(word)):
        answer += word_dict[word[i]] * w[i]
    return answer