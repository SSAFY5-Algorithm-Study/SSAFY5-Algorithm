"""
코드가 너무 더러움.. 수정하겠슴다..
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
        cr, cc = (cr+dr) % len(grid), (cc+dc) % N
        if cr < 0:
            cr = N-1
        if cc < 0:
            cc = N-1
    return dist


def solution(grid):
    global visited, N
    
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    N = len(grid[i])
    
    visited = [[[0]*4 for j in range(len(grid[i]))] for i in range(len(grid))]
    
    answer = []
    for i in range(len(grid)):
        for j in range(N):
            for k in range(4):
                if not visited[i][j][k]:
                    answer.append(find_cycle(i, j, k, grid))

    return sorted(answer)