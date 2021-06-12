N = int(input())
limits = list(map(int, input().split()))
tier = input()

# 각 티어에서 과금할 수 있는 최대 금액을 dict에 저장
tier_max = {'B': limits[0]-1, 'S': limits[1]-1, 'G': limits[2]-1, 'P': limits[3]-1, 'D': limits[3]}


total = current = tier_max[tier[0]]

for i in range(1, len(tier)):
    # 이번달이 다이아 등급일 경우
    if tier[i] == 'D':
        current = limits[3]
    # 두달전이 다이아 등급이었던 경우
    elif current == limits[3]:
        total -= limits[3]
        current = tier_max[tier[i]]
    # 나머지 경우
    else:
        current = tier_max[tier[i]] - current
    total += current

print(total)


# [3
# 30 60 90 150
# BSG