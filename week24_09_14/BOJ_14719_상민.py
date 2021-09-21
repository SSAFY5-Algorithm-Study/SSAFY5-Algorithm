# 가장 큰 수의 인덱스를 기준으로 양쪽을 검사한다.
# 0보다 큰 수를 찾아서 start, end를 설정
# 가장 큰 수의 인덱스가 0이면 end만 설정, -1이면 start만 설정
# 탐색하면서, 0보다 큰 수중 최댓값을 업데이트하면서 result에 +

# 물 웅덩이 계산하는 함수
def calc_water(values):
    # 물 웅덩이 변수 선언, 초기화, 0 할당
    temp = 0
    standard = 0
    for i in range(len(values)):
        # 가지치기
        if values[i] == 0:
            if standard == 0:
                continue
        else:
            if standard == 0 or values[i] >= standard:
                standard = values[i]
                continue
        temp += standard - values[i]
    return temp

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
max_idx = blocks.index(max(blocks))
front, back = blocks[:max_idx + 1], blocks[max_idx:]
print(calc_water(front) + calc_water(back[::-1]))

