'''
19621. 회의실 배정

서준이는 아빠로부터 N개의 회의와 하나의 회의실을 선물로 받았다. 
각 회의는 시작 시간, 끝나는 시간, 회의 인원이 주어지고 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다. 
단, 회의는 한번 시작되면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작 시간은 끝나는 시간보다 항상 작다. 
N개의 회의를 회의실에 효율적으로 배정할 경우 회의를 진행할 수 있는 최대 인원을 구하자.
'''

def DFS(n, people):
    global max_people
    # print('DFS', n, people, max_people)
    
    if n >= N and max_people < people:
        max_people = people
        return
    
    for i in range(n, N):
        # print('for', i, n)
        DFS(i+2, people + meeting[i][2])

# 회의의 수 N
N = int(input())
# 시작 시간, 끝나는 시간, 회의 인원
meeting = [list(map(int, input().split())) for _ in range(N)]
# 먼저 시작하는 회의 순으로 정렬
# 조건 때문에 정렬 안 해도 가능
# meeting.sort()
# 회의 진행하는 최대 인원
max_people = 0
DFS(0, 0)
print(max_people)


'''
[입력]
6
10 40 80
30 60 60
50 80 70
70 100 100
90 120 40
110 140 50

[출력]
230
'''