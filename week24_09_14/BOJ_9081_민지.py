def find_next_word(word):
    pivot = word[-1]
    letters = []

    for i in range(len(word)-2, -1, -1):
        letters.append(pivot)
        if word[i] < pivot:
            letters.append(word[i])
            letters.sort()
            
            for j in range(len(letters)):
                if letters[j] > word[i]:
                    next_letter = letters.pop(j)
                    break

            return word[:i] + next_letter + ''.join(letters)
        else:
            pivot = word[i]
    return word

N = int(input())
for _ in range(N):
    print(find_next_word(input()))


