# 20055. 컨베이어 벨트 위의 로봇 (실버1)

import sys
from collections import deque
input = sys.stdin.readline


def move_conveyor(turn):
    zero = 0
    while True:
        # 1
        belt.appendleft(belt.pop())
        robot.pop()
        robot.appendleft(False)
        if robot[n-1]:
            robot[n-1] = False

        #2
        for i in range(n-2, -1, -1):
            if robot[i] and not robot[i+1] and belt[i+1] >= 1:
                robot[i], robot[i+1] = False, True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    belt[i+1] = -1
                    zero += 1
        if robot[n-1]:
            robot[n-1] = False

        # 3
        if not robot[0] and belt[0] >= 1:
            robot[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                belt[0] = -1
                zero += 1
            
        # 4
        if zero >= k:
            return turn
        turn += 1


n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False]*n)
print(move_conveyor(1))

    
    