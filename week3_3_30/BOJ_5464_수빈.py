'''
5464. 주차장

시내 주차장은 1부터 N까지 번호가 매겨진 N개의 주차 공간을 가지고 있다. 
이 주차장은 매일 아침 모든 주차 공간이 비어 있는 상태에서 영업을 시작하며, 하룻동안 다음과 같은 방식으로 운영된다. 
차가 주차장에 도착하면, 주차장 관리인이 비어있는 주차 공간이 있는지를 검사한다. 
만일 비어있는 공간이 없으면, 차량을 빈 공간이 생길 때까지 입구에서 기다리게 한다. 
만일 빈 주차 공간이 하나만 있거나 또는 빈 주차 공간이 없다가 한 대의 차량이 주차장을 떠나면 곧바로 그 장소에 주차를 하게 한다.
만일 빈 주차 공간이 여러 곳이 있으면, 그 중 번호가 가장 작은 주차 공간에 주차하도록 한다. 
만일 주차장에 여러 대의 차량이 도착하면, 일단 도착한 순서대로 입구의 대기장소에서 줄을 서서 기다려야 한다. 
대기장소는 큐(queue)와 같이, 먼저 대기한 차량부터 주차한다.

주차료는 주차한 시간이 아닌 차량의 무게에 비례하는 방식으로 책정된다. 주차료는 차랑의 무게에다 주차 공간마다 따로 책정된 단위 무게당 요금을 곱한 가격이다.
주차장 관리원은 오늘 M대의 차량이 주차장을 이용할 것이라는 것을 알고 있다. 또한, 차량들이 들어오고 나가는 순서도 알고 있다.
주차 공간별 요금과 차량들의 무게와 출입 순서가 주어질 때, 오늘 하룻동안 주차장이 벌어들일 총 수입을 계산하는 프로그램을 작성하라.
'''
N, M = map(int, input().split())
# 단위 무게당 요금
base_charge = [int(input()) for _ in range(N)]
# 자동차 무게
weight = [int(input()) for _ in range(M)]
weight.insert(0, 0)
# 출입순서
in_out = [int(input()) for _ in range(M*2)]

parking = [0] * N
waiting = []
money = 0

for car in in_out:
    # 음수면 차 빼면서 요금 계산
    if car < 0:
        find = abs(car)
        x = parking.index(find)
        money += base_charge[x] * weight[find]
        parking[x] = 0
        # 기다리는 차가 있으면 그 자리에 주차 시킴
        if waiting:
            parking[x] = waiting.pop(0)
    # 양수면 주차하기
    else:
        # 대기열에 추가
        waiting.append(car)
        for i in range(N):
            if parking[i] == 0:
                parking[i] = waiting.pop(0)
                break
print(money)
'''
[입력]
3 4
2
3
5
200
100
300
800
3
2
-3
1
4
-4
-2
-1

[출력]
5300
'''