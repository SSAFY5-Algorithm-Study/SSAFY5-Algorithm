'''
문제
서준이는 아빠로부터 N개의 회의와 하나의 회의실을 선물로 받았다. 
각 회의는 시작 시간, 끝나는 시간, 회의 인원이 주어지고 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다.
단, 회의는 한번 시작되면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작 시간은 끝나는 시간보다 항상 작다. N개의 회의를 회의실에 효율적으로 배정할 경우 회의를 진행할 수 있는 최대 인원을 구하자.

입력
첫째 줄에 회의의 수 N이 주어진다. 둘째 줄부터 N + 1 줄까지 공백을 사이에 두고 회의의 시작시간, 끝나는 시간, 회의 인원이 주어진다.

출력
첫째 줄에 회의실에서 회의를 진행할 수 있는 최대 인원을 출력한다.
'''


'''
# 런타임에러
def DFS(level, total_people):
    global max_total_people
    # 종료
    if level >= N:
        return
    if max_total_people <= total_people:
        max_total_people = total_people

    for i in range(level+2, N):
    #임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않는다.
        DFS(i, total_people + huei[i][2])

N = int(input())
huei = [list(map(int,input().split())) for _ in range(N)]
huei.sort(key=lambda x:x[0])

total_people = 0
max_total_people = 0
DFS(0,huei[0][2])
DFS(1,huei[1][2])
print(max_total_people)
'''

def DFS(level, total_people):
    global max_total_people
    if level >= N and max_total_people < total_people:
        max_total_people = total_people
        return
    for i in range(level, N):
        DFS(i+2, total_people + huei[i][2])
N = int(input())
huei = [list(map(int, input().split())) for _ in range(N)]
total_people = 0
max_total_people = 0
DFS(0, 0)
print(max_total_people)