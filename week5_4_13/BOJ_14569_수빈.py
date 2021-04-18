'''
14569. 시간표 짜기

연세대학교 수강신청 기간이 시작되었다. 
많은 친구들은 비어 있는 시간에 어떤 과목을 추가로 신청할 수 있는지를 궁금해 한다.
이 친구들이 비어 있는 시간에 추가로 신청할 수 있는 과목의 후보 개수를 구해보자.
후보 개수를 세는 것이므로 현재 내 시간표에서 신청할 수 있는 과목끼리 시간이 겹치더라도 모두 세어야 한다.
즉, 월요일 1, 2, 3, 4, 5교시 시간이 비어 있고 한 과목의 시간이 월요일 1, 2, 3, 4교시이고 나머지 한 과목의 시간이 월요일 2, 3, 4, 5교시라면 2과목 모두 후보가 될 수 있다.
'''
# N = int(input())
# lectures = [list(map(int, input().split())) for _ in range(N)]
# M = int(input())
# students = [list(map(int, input().split())) for _ in range(M)]

# # 삼중 for문 / 하나씩 다 검사 -- 비효율...
# for student in students:
#     cnt = 0
#     for i in range(N):
#         # 과목의 수업시간 수가 비어있는 교시 개수보다 크면 수강하지 못한다.
#         if lectures[i][0] > student[0]:
#             break
#         for j in range(1, N):
#             if lectures[i][j] not in student:
#                 break
#         else:cnt += 1
#     print(cnt)


# set - 교집합 이용?!
N = int(input())
lectures = [set(list(map(int, input().split()))[1:]) for _ in range(N)]
M = int(input())
students = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

for student in students:
    cnt = 0
    for i in range(N):
        if lectures[i].intersection(student) == lectures[i]:
            cnt += 1
    print(cnt)
'''
[입력]
3
4 1 2 3 4
6 5 6 7 8 9 10
4 11 21 31 41
5
8 1 2 3 4 5 6 7 8
7 1 2 3 7 8 9 10
14 1 2 3 4 5 6 7 8 9 10 11 21 31 41
5 41 42 43 44 45
10 1 5 6 7 8 9 10 11 21 31

[출력]
1
0
3
0
1
'''