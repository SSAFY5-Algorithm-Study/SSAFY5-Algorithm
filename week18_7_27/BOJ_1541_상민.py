input_string = input()
new = input_string.split('-')
for idx, temp in enumerate(new):
    new_new = temp.split('+')
    sum_value = sum(list(map(int, new_new)))
    if idx == 0:
        answer = sum_value
    else:
        answer -= sum_value
print(answer)