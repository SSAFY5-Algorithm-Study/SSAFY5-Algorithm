'''
1946. 신입 사원

언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 
인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 
최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.

그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다.
즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.
'''

# 얘는 시간 초과
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 지원자의 수
    N = int(input())
    grades = [list(map(int, input().split())) for _ in range(N)]
    cnt = N
   
    for i in range(N):
        A_resume, A_interview = grades[i]
        for j in range(N):
            B_resume, B_interview = grades[j]
            if A_resume > B_resume and A_interview > B_interview:
                print(grades[i], [grades[j]])
                cnt -= 1
                break
    print(cnt)
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 지원자의 수
    N = int(input())
    grades = [list(map(int, input().split())) for _ in range(N)]
    # 일단 서류심사 성적 순으로 정렬 시키고 면접 성적만 비교하기 위해서 정렬!
    grades.sort(key = lambda x:x[0])
    base = grades[0][1]
    # 서류 심사가 1등인 애는 바로 뽑으면 되기 때문에 1로 설정한다.
    cnt = 1
    for i in range(1, N):
        # 이전 사람의 면접 등수와 본인의 면접 등수 중 더 높은 값이 기준이 된다.
        # 등수가 더 높으면 숫자는 작아야하기 때문에 min사용
        base = min(base, grades[i][1])
        # 만약 기준이 본인의 면접 등수라면 선발된다.
        if base == grades[i][1]:
            cnt += 1
    print(cnt)
'''
[입력]
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1

[출력]
4
3
'''