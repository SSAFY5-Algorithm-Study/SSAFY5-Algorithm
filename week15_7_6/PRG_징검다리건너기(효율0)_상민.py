'''
아이디어
-> 다음 칸이 0인지 계속 파악하고 앞으로 가기
    - 0이면 -> stone +=1 -> k > stone인 상황에서 0이 아닌 것을 만났을 때는 가능
                                             -> 0을 만나면 불가능
-> 건너면 디딤돌 -1
'''

def solution(stones, k):
    answer = 0
    while True:
        zero_cnt = 0
        for i in range(len(stones)):
            # 0이 아닌 경우
            if stones[i]:
                stones[i] -= 1
                zero_cnt = 0
            # 0인 경우
            else:
                zero_cnt += 1
                if zero_cnt >= k:
                    return answer
        else:
            answer += 1
    return answer