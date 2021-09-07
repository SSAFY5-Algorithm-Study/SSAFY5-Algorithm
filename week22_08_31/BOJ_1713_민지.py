N = int(input())
M = int(input())

recommendations = list(map(int, input().split()))

recommended = [-1] * M # 현재 추천 된 학생들을 저장할 배열
time = 0 # 추천 되는 시점
votes = [0] * M
cnt = 0

def find_lowest_votes():
    lowest_votes = 10000000000
    lowest_idx = 0
    lowest_time = 1000000000

    for i in range(M):
        if recommended[i] != -1:
            if votes[i] > lowest_votes:
                continue
            elif votes[i] == lowest_votes and recommended[i] > lowest_time:
                continue

            lowest_idx = i
            lowest_votes = votes[i]
            lowest_time = recommended[i]

    return lowest_idx
            


for i in recommendations:
    time += 1
    cnt += 1
    if recommended[i] == -1:
        if cnt > N:
            lowest_idx = find_lowest_votes()
            recommended[lowest_idx] = -1
            cnt -= 1
        recommended[i] = time
    votes[i] += 1

result = []
for i in range(M):
    if recommended[i] != -1:
        result.append(i)
        
print(*result)