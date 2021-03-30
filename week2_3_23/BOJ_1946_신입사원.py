import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = sorted(list(map(int, input().split())) for _ in range(N))
    # 둘 중에 하나라도 작은 점수가 있으면 뽑을 수 없다.
    # 그래서 서류 점수(0번째 인덱스값)으로 1~N등까지 나열한 후
    # 0 ~ N 순서로 면접 점수를 비교하면서 진행 (서류 1등은 무조건 뽑는 전제)
    standard = scores[0][1]
    cnt = 1
    for score in scores:
        if score[1] >= standard:
            continue
        else:
            cnt += 1
            standard = score[1]
    print(cnt)

