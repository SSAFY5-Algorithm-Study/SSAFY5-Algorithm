"""
변수 설명
grid: 타일을 한 글자씩 저장해 놓은 2차원 배열
[
    ['S', 'L'],
    ['L', 'R']
]
visited: 각 타일 별로 상/하/좌/우 네방향에서 빛이 통과한 적이 있는지 검사하는 3차원 배열
[
    [[0,0,0,0], [0,0,0,0]],
    [[0,0,0,0], [0,0,0,0]]
]
cr, cc: 현재 위치 (row, column)
cd: 현재 타일로 올때 빛이 날아온 방향
dist: 현재 사이클의 총 길이

LR: length row - 총 행의 갯수
LC: length col - 총 열의 갯수
"""
# 상하좌우 순서대로 해당 방향에서 빛이 날아왔을때,
# 반사 빛이 어디로 이동하는지를 저장해 놓은 dict
# 0: 상, 1: 하, 2: 좌, 3: 우
# 예시) direction['L'][0] = 위에서 내려온 빛이 L 타일을 만났을 때 꺾이는 방향 --> [0,1] --> 오른쪽으로 한칸 이동
direction = {
    'S': [[1,0,0], [-1,0,1], [0,1,2], [0,-1,3]],
    'L': [[0,1,2], [0,-1,3], [-1,0,1], [1,0,0]],
    'R': [[0,-1,3], [0,1,2], [1,0,0], [-1,0,1]]
}


def find_cycle(cr, cc, cd, grid):
    dist = 0
    while visited[cr][cc][cd] == 0:
        visited[cr][cc][cd] = 1
        dist += 1
        node = grid[cr][cc]
        
        # 그 다음 이동할 칸
        dr, dc, cd = direction[node][cd]
        cr, cc = (cr+dr) % LR, (cc+dc) % LC
    return dist


def solution(grid):
    global visited, N, LR, LC

    LR = len(grid)
    LC = len(grid[0])
    
    # 사용하기 편하게 grid의 각 글자를 한글자씩 떼어주기
    for i in range(LR):
        grid[i] = list(grid[i])
    
    # 3차원 visit 배열 생성
    visited = [[[0]*4 for _ in range(LC)] for _ in range(LR)]
    
    answer = []
    # 아직까지 방문하지 않은 노드+방향 조합이 있다면, 그 곳을 시작점으로 해서 탐색 시작
    for i in range(LR):
        for j in range(LC):
            for k in range(4):
                if not visited[i][j][k]:
                    answer.append(find_cycle(i, j, k, grid))
                    
    return sorted(answer)