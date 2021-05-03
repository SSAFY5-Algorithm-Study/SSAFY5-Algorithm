'''
문제
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

입력
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하이고, D는 10,000보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.

출력
세준이가 운전해야하는 거리의 최솟값을 출력하시오.
'''

#접근 : 도착위치 - 시작위치가 지름길 길이보다 작다? 지름길 아니다!
# 10001개 배열 만들어 놓고, 하나씩 다 찾아가면서 작은값을 집어넣기.
# 실패 대실패
# 다익스트라로?

# N <= 12, D <= 10000
N, D = map(int, input().split())

shortpath_list = []
for _ in range(N):
    # 시작위치, 도착위치, 지름길의 길이
    s, e, cut = map(int, input().split())
    if cut >= e - s:
        continue
    shortpath_list.append([s,e,cut])

shortpath_list.sort(key=lambda x: (x[0],x[1]))


move = 0
move_list = [0] + ([10001] * 10000)
print(len(move_list))
print(shortpath_list)
i = 0
while move < D:
    if i < len(shortpath_list):
        shortpath = shortpath_list[i]
        if move == shortpath[0]:
            move_list[shortpath[1]] = min(move_list[move] + shortpath[2], move_list[shortpath[1]])
            i += 1
        else:
            move_list[move+1] = min(move_list[move+1], move_list[move] + 1)
            move += 1
    else:
        move_list[move+1] = min(move_list[move+1], move_list[move] + 1)
        move += 1

print(move_list[D])


