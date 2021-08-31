mode = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def change_mode(letter, current_mode):
    if letter == 'D':
        return (current_mode + 1) % 4
    return (current_mode + 3) % 4
        

N = int(input())
K = int(input())
apple_location = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
change_info = [input().split() for _ in range(L)]

print(apple_location, change_info)