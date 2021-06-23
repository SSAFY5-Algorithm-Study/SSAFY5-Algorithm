'''
하나의 이닝은 공격과 수비로 이루어지고 -> N이닝 게임 진행
한 이닝에 3아웃 -> 이닝 종료 -> 공수 변경
1번 타자 -> 4번째 순서 고정
가장 점수가 높은 경우 찾기
'''

# 뭐지 왜틀리지.

def sumsum():
    num = 0     #이닝 번호
    out = 0     #아웃 카운트
    temp = tasoon[1]-1 #현재 선수
    score = 0   # 점수
    i = 1   # 현재 순서
    roo = [0] * 4
    while num < N:
        # 아웃
        if ining[num][temp] == 0:
            out += 1
        # 1루타
        elif ining[num][temp] == 1:
            if roo[3]:
                roo[3] = 0
                score += 1
            if roo[2]:
                roo[2] = 0
                roo[3] = 1
            if roo[1]:
                roo[2] = 1
                roo[1] = 0
            roo[1] = 1
        elif ining[num][temp] == 2:
            if roo[3]:
                roo[3] = 0
                score += 1
            if roo[2]:
                roo[2] = 0
                score += 1
            if roo[1]:
                roo[3] = 1
                roo[1] = 0
            roo[2] = 1
        elif ining[num][temp] == 3:
            if roo[3]:
                roo[3] = 0
                score += 1
            if roo[2]:
                roo[2] = 0
                score += 1
            if roo[1]:
                roo[1] = 0
                score += 1
            roo[3] = 1
        else:
            if roo[3]:
                score += 1
                roo[3] = 0
            if roo[2]:
                score += 1
                roo[2] = 0
            if roo[1]:
                score += 1
                roo[1] = 0
            score += 1
        if out == 3:
            break
        if i == 9:
            i = 1
        else:
            i += 1
        temp = tasoon[i]-1
    return score


def DFS(order):
    if order == 10:
        global max_point
        result = sumsum()
        if result > max_point:
            max_point = result
        return
    for i in range(2, 10):
        if check_tasoon[i] == True:
            continue
        check_tasoon[i] = True
        tasoon[order] = i

        if order == 3:
            DFS(order + 2)
        else:
            DFS(order + 1)
        check_tasoon[i] = False
        tasoon[order] = 0



N = int(input())
ining = [list(map(int,input().split())) for _ in range(N)]
check_tasoon = [False] * 10
tasoon = [0] * 10
# 4번 타자 : 1
tasoon[4] = 1
max_point = 0
DFS(1)
print(max_point)