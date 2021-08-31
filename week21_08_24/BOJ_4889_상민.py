output = []
idx = 0

pairs = {
    '{': '}',
}

pairs_score = {
    '{': { 
        '}': 0,
        '{': 1
    },
    '}': {
        '{': 2, 
        '}': 1
    }
}

while True:
    remainder_stack = []
    current_input = input()
    answer = 0
    idx += 1
    # print(answer, idx)
    if '-' in current_input:
        break
    for i in range(len(current_input)):
        if i == 0 or not remainder_stack:
            remainder_stack.append(current_input[i])
        else:
            top_stack = remainder_stack[-1]
            if pairs.get(top_stack) == current_input[i]:
                remainder_stack.pop()
            else:
                remainder_stack.append(current_input[i])
    #print(remainder_stack, 'remainder_stack', idx)

    for i in range(0, len(remainder_stack), 2):
        element1 = remainder_stack.pop(0)
        element2 = remainder_stack.pop(0)
        answer += pairs_score[element1][element2]
    output.append((idx, answer))
# print(output)
[print(f'{index}. {num}') for (index, num) in output]
        