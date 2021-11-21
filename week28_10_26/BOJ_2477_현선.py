melon = int(input())

max_height = 0
max_width = 0
direction_list = []
length_list = []
area = [0] * 7
for i in range(6):
    direction, length = map(int,input().split())
    direction_list.append(direction)
    length_list.append(length)
    if direction == 1 or direction == 2:
        if length > max_width:
            max_width = length
    else:
        if length > max_height:
            max_height = length
 
result = 0
for i in range(5):
    area[i] = length_list[i] * length_list[i+1]
    result += area[i]
area[6] = length_list[0] * length_list[5]
result += area[6]
result -= max_width * max_height * 2
print(result * melon)