'''
아이디어
-> 세로, 가로를 돈다 (N만큼)
X를 만나기 전에 space가 2이상이면 ans += 1
2 미만이면 space 초기화 ->
'''

N = int(input())
room = list(input() for _ in range(N))
possible_width = 0
possible_height = 0

# i=열
for i in range(N):
    height_temp = 0
    width_temp = 0
    # j=행
    for j in range(N):
        # room[0][0], room[1][0] -> 세로(height)
        if room[j][i] == '.':
            height_temp += 1
        else:
            if height_temp >= 2:
                possible_height += 1
            height_temp = 0

        if room[i][j] == '.':
            width_temp += 1
        else:
            if width_temp >= 2:
                possible_width += 1
            width_temp = 0
    if height_temp >= 2:
        # print('plus')
        possible_height += 1

    if width_temp >= 2:
        possible_width += 1


print(possible_width, possible_height)

