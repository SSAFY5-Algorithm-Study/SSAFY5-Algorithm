'''
list.pop(0)은 첫 번째 요소를 pop한 후 나머지 요소를 앞으로 한 칸씩 당기므로 O(N)의 시간이 걸린다.
상관 없다면 list.pop()을 사용하자.
큐를 활용할 때 리스트를 이용하는 것보다 deque가 눈에 띌 정도로 빠르다. O(1)
표준 라이브러리를 적극적으로 활용하자
'''
from collections import deque

import sys
sys.stdin = open('input.txt')


dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 토마토가 익어있는 상태와 토마토가 모두 익지 못하는 상황 찾는 함수
def find_situations():
    # 아직 덜 익은 토마토 개수 초기화
    zero_count = 0
    # 농장을 샅샅이 뒤진기 시작
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            # 덜 익은 토마토가 있으면
            if farm[i][j] == 0:
                # 토마토가 들어있지 않은 칸 초기화
                minus_count = 0
                # +1
                zero_count += 1
                # 상하좌우 이동하면서 토마토 확인
                for r, c in dxy:
                    nr = i + r
                    nc = j + c
                    # 토마토가 들어있지 않으면
                    if farm[nr][nc] == -1:
                        # +1
                        minus_count += 1
                        # 사방에 토마토가 없으면
                        if minus_count == 4:
                            # 토마토가 익지 못하는 상황 : -1 리턴
                            return -1
            # 익은 토마토라면
            elif farm[i][j] == 1:
                # 시작 위치에 추가
                one_location.append((i, j, 0))
    # 더이상 익을 토마토가 없으면
    if zero_count == 0:
        # 0 리턴
        return 0


def BFS(ones):
    queue = deque()
    cnt = 0
    queue = ones
    # 토마토가 있는 지역에는 미리 발견 표시 해줌
    for y, x, z in queue:
        discovered[y][x] = 1
    while queue:
        cr, cc, cnt = queue.popleft
        for r, c in dxy:
            nr = cr + r
            nc = cc + c
            if farm[nr][nc] == 0 and not discovered[nr][nc]:
                discovered[nr][nc] = 1
                queue.append((nr, nc, cnt + 1))
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # -1로 padding
    farm = [[-1] + list(map(int, input().split())) + [-1] for _ in range(M)]
    farm.insert(0, [-1] * (N + 2))
    farm.append([-1] * (N + 2))
    # 1의 위치를 담을 빈 리스트 생성 (1은 익은 토마토의 위치)
    one_location = []
    # 익어진 토마토 위치 저장할 빈 리스트
    discovered = [[0] * (N + 2) for _ in range(M + 2)]
    # 토마토가 익어있는 상태와 토마토가 모두 익지 못하는 상황 찾는 함수 실행
    ans = find_situations()
    if ans:
        print(ans)
    # 위의 두 가지의 상황이 아니면
    else:
        # BFS 시작
        print(BFS(one_location))