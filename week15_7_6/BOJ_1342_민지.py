def is_lucky_word(level, prev, word):
    if level == N:
        word_set.add(word)
        return

    for i in range(N):
        if not visited[i] and raw[i] != prev:
            visited[i] = 1
            is_lucky_word(level+1, raw[i], word+raw[i])
            visited[i] = 0


raw = input()
word_set = set()
N = len(raw)
cnt = 0
visited = [0] * 10

if N == len(set(raw)):
    print(factorial(N))
else:        
    for i in range(N):
        visited[i] = 1
        is_lucky_word(1, raw[i], raw[i])
        visited[i] = 0

    print(len(word_set))