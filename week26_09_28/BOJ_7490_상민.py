def calc(cur_mode, given_list):
    value, order = given_list
    next_order = order + 1
    if cur_mode == '+':
        return [value + '+' + str(next_order), next_order]
    if cur_mode == '-':
        return  [value + '-' + str(next_order), next_order]
    if cur_mode == '++':
        return [value + ' ' + str(next_order), next_order]

modes = ('+', '-', '++')

def BFS(max_length):
    queue = [['1', 1]]
    while queue:
        cur_list = queue.pop(0)
        for mode in modes:
            new_list = calc(mode, cur_list)
            if new_list[1] >= int(max_length):
                if eval(new_list[0].replace(' ', '')) == 0:
                    result.append(new_list[0])
            else:
                queue.append(new_list)


N = int(input())
nums = [input() for _ in range(N)]
for idx, num in enumerate(nums):
    result = []
    BFS(num)
    print('\n'.join(sorted(result)))
    if idx != N - 1:
        print()
