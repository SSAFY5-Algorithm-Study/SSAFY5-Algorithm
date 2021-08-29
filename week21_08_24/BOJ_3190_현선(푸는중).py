n = int(input())
k = int(input())
apples = [list(map(int ,input().split())) for _ in range(k)]
l = int(input())
direction = [list(input().split()) for _ in range(l)]
cnt = 0
board = [[0 for _ in range(n)] for _ in range(n)]
# 사과 배치
for i in range(k):
    board[apples[i][0]-1][apples[i][1]-1] = 2
board[0][0] = 1
print(board)
snake_length = 1

# 최초에는 길이가 1이니까
snake_position = [[0, 0]]
move = [0, 1]
c_cnt, c_direction = direction.pop(0)
while True:
    
    if cnt == int(c_cnt):
        if move == [0,1]:
            if c_direction == 'D':
                move = [1,0]
            elif c_direction == 'L':
                move = [-1,0]
        elif move == [1,0]:
            if c_direction == 'D':
                move = [0,1]
            elif c_direction == 'L':
                move = [0,-1]
        elif move == [0, -1]:
            if c_direction == 'D':
                move = [-1,0]
            elif c_direction == 'L':
                move = [1,0]
        elif move == [-1,0]:
            if c_direction == 'D':
                move = [0,1]
            elif c_direction == 'L':
                move = [0,-1]
        if len(direction):
            c_cnt, c_direction = direction.pop(0)
    
    r,c = snake_position[0]
    r += move[0]
    c += move[1]
    if 0 <= r < n and 0 <= c < n and [r,c] not in snake_position:
        if board[r][c] == 2:
            snake_position.insert(0,[r,c])
        else:
            snake_position.insert(0,[r,c])
            snake_position.pop(-1)
    else:
        break
    cnt += 1
print(cnt)