word1 = input()
word2 = input()

def initialize_dict(word, n):
    word_dict = {}
    for i in range(n):
        word_dict[i] = word_dict.get(word[i], 0) + 1
    return word_dict

def check_interval_component(n):
    word1_dict = initialize_dict(word1, n)
    word2_dict = initialize_dict(word2, n)




length = min(len(word1), len(word2))

for i in range(length, 0, -1):
    check_interval_component(i)