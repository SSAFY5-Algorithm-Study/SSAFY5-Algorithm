N = int(input())
limits = list(map(int, input().split()))
tier = input()

# 각 티어에서 과금할 수 있는 최대 금액을 dict에 저장
tier_max = {'B': limits[0]-1, 'S': limits[1]-1, 'G': limits[2]-1, 'P': limits[3]-1}


total = current = tier_max[tier[0]]

for i in range(1, len(tier)):
    current = 500 if tier[i] == 'D' else tier_max[tier[i]] - current
    total += current

print(total)