N, M = map(int, input().split())
parking_prices = list(int(input()) for _ in range(N))
car_weights = [0] + list(int(input()) for _ in range(M)) # padding을 줘서 1,2,3,4 indexing 가능하게 만듬
car_orders = list(int(input()) for _ in range(M * 2))
parking_spaces = [0] * N

# 주차장 크기
parking_nums = len(parking_spaces)
# 수입 초기화
income = 0
# 주차대기열 생성 / queue
waiting = []
# 미리 알려진 자동차 입장 순서에서 첫 번째 순서부터 진행
for order in car_orders:
    # 주차하는 차량(+)이고
    if order > 0:
        # 주차장에 자리가 없으면
        if 0 not in parking_spaces:
            # 대기열에 넣어둠
            waiting.append(order)
            continue
        # 주차
        # 비어있는 주차 구역 파악
        for i in range(parking_nums):
            # 파악 완료
            if parking_spaces[i] == 0:
                # 주차 시켜줌
                parking_spaces[i] = order
                break
    # 출차하는 차량이면
    elif order < 0:
        # 어디 구역에 주차되어 있는 지 찾는 과정
        for j in range(parking_nums):
            # 찾았다면
            if parking_spaces[j] == -order:
                # 출차와 동시에 우선순위 대기열에 있는 차량 주차
                if waiting:
                    parking_spaces[j] = waiting.pop(0)
                # 대기열이 없으면 해당 주차공간 비어있다고 표시
                else:
                    parking_spaces[j] = 0
                # 주차요금 정산
                income += (car_weights[-order] * parking_prices[j])
                break
print(income)