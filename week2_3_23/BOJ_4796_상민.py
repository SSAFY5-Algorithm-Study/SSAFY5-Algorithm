import sys
sys.stdin = open('input.txt')

# while문을 돌리기 위해 첫 input값을 받고 시작
L, P, V = map(int, input().split())
# case 번호 표시하기 위해 i 선언
i = 0
# input 마지막 줄에 0, 0, 0이 나와야 끝이므로
# 끝이 어딘지 모르기 때문에 while문 사용, L, P, V 셋 다 0으로 끝나서
# 셋 중 하나라도 0일때가지만 반복문 돌아가도록 설정
while V != 0:
    # case 번호 + 1
    i += 1
    # 매 input마다 답 초기화
    ans = 0
    # V로 P를 나눈 몫, 나머지 구하기
    share, remainder = divmod(V, P)
    # 몫 * L (V일이 주어지면 L일만큼 쉴 수 있다해서)
    ans += share * L
    # 남은 요일이 L보다 많으면 
    if remainder > L:
        # L만큼만 캠핑
        ans += L
    # 남은 요일이 적거나 같으면 나머지를 더해줌
    else:
        ans += remainder
    print('Case %d: %d' % (i, ans))
    L, P, V = map(int, input().split())