# BOJ 3699 주차빌딩
"""
변수 설명
F = 총 층의 갯수
C = 층별 차 댓수
floor = 현재 층
building = 주차장의 차 위치를 담은 이중 배열
cars = 차의 위치를 저장해 놓은 딕셔너리 (k:차 번호, v: 위치 리스트[r, c])
time = 총 걸리는 시간
time_c = 특정 차 한대를 뽑아오는데 걸리는 시간
"""
import sys
sys.stdin = open('3699_input.txt', 'r')

T = int(input())

def update_location(floor):
    global cars
    for j in range(C):
        if building[floor][j] != -1:
            cars[building[floor][j]] = [floor, j]


def get_car(row, col):
    # 올라갔다 내려오는 시간
    time_c = 2 * row * 10
    # 차가 리스트의 앞쪽 반에 있다면 왼쪽으로 이동
    if col <= C // 2:
        # 빌딩 맨 앞에 있는 차를 뽑아서 맨 끝으로 보내기
        for _ in range(col):
            front = building[row].pop(0)
            building[row].append(front)
        return time_c + col * 5
    # 차가 리스트의 뒤쪽 반에 있다면 오른쪽으로 이동
    # C - col 횟수만큼 이동해야된다
    else:
        for _ in range(C-col):
            back = building[row].pop()
            building[row].insert(0, back)
        return time_c + (C-col) * 5


for tc in range(1, T+1):
    F, C = map(int, input().split())
    building = [list(map(int, input().split())) for _ in range(F)]
    cars = {}
    time = 0

    # 맨 처음 차의 위치를 저장해놓기
    # 각 층을 순회하면서 -1이 아닌 숫자가 나왔을때
    for floor in range(F):
        update_location(floor)
    
    # 총 몇대의 차가 있는 계산
    N = max(cars.keys())
    # 1번부터 차를 꺼내오기
    for car in range(1, N+1):
        # cars 딕셔너리에서 차의 위치 가져오기
        row, col = cars[car]
        time += get_car(row, col)
        # 다른 차들의 위치도 바뀌었으니 그 층에 있는 차의 위치 업데이트
        update_location(row)

    print(time)
