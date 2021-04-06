"""
변수 설명
parking_lot = 주차장
prices = 각 칸별 가격
weights = 각 차의 무게
order = 나갔다 들어왔다 하는 순서
cars = 각 차가 주차된 위치
car = 현재 차의 인덱스
profit = 총 수익

"""
import sys
sys.stdin = open('5464_input.txt', 'r')


def car_enter(car):
    global profit
    global queue

    # 주차장을 맨 앞부터 순회하면서
    for i in range(N):
        # 주차장에 빈칸이 있으면 주차
        if not parking_lot[i]:
            parking_lot[i] = 1
            cars[car] = i
            profit += weights[car] * prices[i]
            return
    # 주차장에 빈칸이 하나도 없었을 경우
    else:
        queue.append(car)


def car_exit(car):
    global profit

    location = cars[abs(car)]
    parking_lot[location] = 0
    # 대기열에 있던 차가 있는 경우
    if queue:
        new_car = queue.pop(0)
        parking_lot[location] = 1
        cars[new_car] = location
        profit += weights[new_car] * prices[location]

N, M = map(int, input().split())
parking_lot = [0] * N
prices = [int(input()) for _ in range(N)]
weights = [0] + [int(input()) for _ in range(M)]
order = [int(input()) for _ in range(2*M)]
cars = {}
queue = []
profit = 0

for car in order:
    # 차가 들어오는 상황
    if car > 0:
        car_enter(car)
    # 차가 나가는 상황
    else:
        car_exit(car)


print(profit)
