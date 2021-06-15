'''
아이디어
- 더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움을 요청한다.
    -> 1. 자기보다 작은 물고기가 없을 때 (ex. 상어크기 = 2, 다른 물고기들 >= 3)
    -> 2. 물고기 자체가 없을 때 (상어빼고 나머지가 0)

- 먹을 수 있는 물고기 ==  1마리면, 해당 물고기에게 가고
- 먹을 수 있는 물고기 >= 2마리면, 거리가 가장 가까운 물고기를 먹으러 간다. (BFS)
    -> 거리가 가까운 물고기가 많다면, 가장 위 -> 가장 왼쪽의 물고기를 먹는다 (dxy = 상, 좌, 우, 하순)

- 물고기를 먹으면, 그 칸은 빈 칸이 된다
    -> 해당 칸을 0으로 만들어줌

- 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기 1 증가
    -> shark_size(상어 크기) += 1 if eaten_fish(먹은 물고기 개수) == 상어 크기
    -> 상어 크기가 커지면, eaten_fish = 0


- 출력: 몇 초동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하여라
    == 아기 상어가 물고기를 먹을 수 있는 최대 시간은 얼마인가
    -> 매번 상어가 물고기를 먹고나서, 현재 먹을 수 있는 물고기가 있는 지 파악 필요

'''

# 상, 좌, 우, 하
dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_shark_and_fish():
    for i in range(N):
        for j in range(N):
            temp = sea[i][j]
            if temp:
                if temp == 9:
                    shark_location.append(i)
                    shark_location.append(j)
                else:
                    # 물고기 크기 배열
                    fish_sizes.append(temp)
                    # 물고기 위치 정보
                    fish_locations.append((i, j))

def BFS(start_node):
    discovered = [[0] * N for _ in range(N)]
    # 시작 노드 발견 처리
    sr, sc = start_node
    discovered[sr][sc] = 1
    queue = [(sr, sc, time[0])]
    while queue:
        cr, cc, spent_time = queue.pop(0)
        for r, c in dxy:
            nr = cr + r
            nc = cc + c
            spent_time += 1
            # 범위 내에 있고 아직 발견되지 않은 것들
            if 0 <= nr < N and 0 <= nc < N and not discovered[nr][nc]:
                # 상어가 통행 불가능한 곳이면
                if sea[nr][nc] > shark_size[0]:
                    continue
                # 상어보다 물고기 크기가 작으면
                # 즉, 먹을 수 있으면
                elif 0 < sea[nr][nc] < shark_size[0]:
                    shark_size[1] += 1
                    # 상어 크기 성장
                    if shark_size[0] == shark_size[1]:
                        shark_size[0] += 1
                        shark_size[1] = 0
                    print(sea[nr][nc], nr, nc)
                    print(fish_sizes)
                    # 바다에서 물고기 제거
                    sea[nr][nc] = 0

                    # 시간 플러스
                    time[0] += spent_time
                    return

                # 나머지 경우 (크기가 같을 때)
                # 현재 상어 크기이하이면 통행 가능
                elif sea[nr][nc] == shark_size[0]:
                    queue.append((nr, nc, spent_time))
                    # 발견 처리
                    discovered[cr][cc] = 1


# 기본 설정
# N x N
N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
fish_locations = []
shark_location = []
# 물고기 사이즈
fish_sizes = []
# 상어 사이즈
shark_size = [2, 0]
# 시간
time = [0]


# 알고리즘

# 상어와 물고기 위치 찾기
find_shark_and_fish()

while True:
    # 물고기가 없으면 break
    if not fish_locations:
        break
    # 최소 물고기 사이즈가 상어의 크기보다 크면 break
    if min(fish_sizes) >= shark_size[0]:
        break
    BFS(shark_location)
    # 더 이상 상어의 크기보다 작은 물고기가 없으면 끝낸다.

print(time[0])