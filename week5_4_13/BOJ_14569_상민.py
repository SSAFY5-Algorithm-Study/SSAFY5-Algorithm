import sys
sys.stdin = open('input.txt')

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]
# 학생 한 명씩 뽑아서
for student in students:
    # 가능한 시간대를 set으로 만듬
    student2 = set(student[1:])
    # 후보 갯수 초기화
    cnt = 0
    # 수업 하나씩 비교
    for clss in classes:
        # 수업시간 set으로 만듬
        clss2 = set(clss[1:])
        # 수업시간이 가능하면
        # clss2: {1, 2, 3, 4}
        # student2: {1, 2, 3, 4, 5, 6, 7, 8}
        # clss2 - student2 => set() => false
        #                  => not set() => true (시간표로 등록이 불가능하다)
        if not clss2 - student2:
            # 후보 + 1
            cnt += 1
    print(cnt)

