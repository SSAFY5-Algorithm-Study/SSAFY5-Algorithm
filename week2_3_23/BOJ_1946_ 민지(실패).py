T = int(input())
for tc in range(T):
    N = int(input())
    applicants = []
    for _ in range(N):
        applicants.append(list(map(int, input().split())))
    
    applicants = sorted(applicants, key=(lambda x: (x[0], x[1])))
    
    max_cnt = 1
    min_score = applicants[0]
    for applicant in applicants[1:]:
        if (applicant[0] <= min_score[0]) or (applicant[1] <= min_score[1]):
            max_cnt += 1
            max_score = applicant
    print(max_cnt)
