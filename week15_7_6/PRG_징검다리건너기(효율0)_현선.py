def solution(stones, k):
    answer = 0
    flag = 1
    while flag:
        # 건너는 인원 증가
        answer += 1
        # 사람 건너면 1씩 숫자 줄어듬
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            stones[i] -= 1
        # 연속해서 0가 몇개인지 체크
        cnt = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                cnt += 1
                if cnt == k:
                    flag = 0
                    break
            else:
                cnt = 0
    return answer