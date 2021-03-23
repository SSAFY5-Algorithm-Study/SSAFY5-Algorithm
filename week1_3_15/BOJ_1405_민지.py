# 동서남북 순으로 drc 설정
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 확률 최댓값 1에서 시작
ans = 1

# cr, cc: 현재 row, col 위치
# visited: 현재까지 지나온 경로
# prob: 현재 경로로 올 가능성
# level: 몇번째 move인지
def move(cr, cc, visited, prob, level):
    # N 만큼 이동 후 아직까지 겹치는 길로 이동하지 않았다면 재귀 탈출
    if level >= N:
        return
   
    # 현재 위치를 경로에 추가
    visited.append([cr, cc])
    # 현재 위치를 기준으로 사방탐색
    for i in range(4):
        nr, nc = cr+dr[i], cc+dc[i]
        # 중복 되는 길을 갔을 경우, 그 길을 가게 될 확률 만큼 전체에서 빼주고 재귀 탈출
        if [nr, nc] in visited:
            global ans
            ans -= prob*prob_arr[i]
            # 이 부분에서 continue가 아니라 return을 한게 문제였음
            continue
        # 그렇지 않은 경우 다음 칸으로 이동하고 다시 재귀 호출
        move(nr, nc, visited, prob*prob_arr[i], level+1)
    # deepcopy 대신 visit 배열에 넣었다 빼는 형식으로 시간 절약
    visited.pop()

# 경우의 수를 담은 배열과, 타겟 이동 횟수 N 받아오기
prob_arr = list(map((lambda x: float(x)), input().split()))
N = prob_arr.pop(0)
prob_arr = [0.01*i for i in prob_arr]

move(0, 0, [], 1, 0)

print(ans)
