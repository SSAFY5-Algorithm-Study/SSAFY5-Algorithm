N = int(input())
input_string = input()
word = 'pPAp'

idx = 0
answer = 0
while idx < N -3:
    if input_string[idx:idx+4] == word:
        answer += 1
        idx += 4
    else:
        idx += 1
print(answer)
    
