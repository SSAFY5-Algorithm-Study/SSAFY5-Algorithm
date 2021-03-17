import sys
sys.stdin = open('19621_input.txt', 'r')

max_ppl = 0
def find_max(k, total):
    global max_ppl
    # 종료 조건: 현재 인덱스가 N보다 큰 경우(회의중에 해당되는 인덱스가 없기 때문에 종료)
    if k >= N:
        if total > max_ppl:
            max_ppl = total
        return

    # 아닐 경우 2번째, 3번째 뒤 회의를 추가하는 재귀 함수 호출
    total += ppl[k]    
    find_max(k+2, total)
    find_max(k+3, total)
 

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
ppl = [meeting[2] for meeting in meetings]

# 시작점이 0 또는 1일 경우 두가지를 호출
find_max(0, 0)
find_max(1, 0)
print(max_ppl)