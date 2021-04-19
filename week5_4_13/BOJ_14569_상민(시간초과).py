N = int(input())
classes = sorted(list(map(int, input().split())) for _ in range(N))
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]
# 시간초과
for student in students:
    temp = []
    cnt = 0
    for clss in classes:
        for clss_detail in clss[1:]:
            if clss_detail not in student[1:]:
                break
            temp += [clss_detail]
        else:
            for t in temp:
                student[1:].remove(t)
            cnt += 1
    print(cnt)
