"""
BOJ 9655. 돌게임

돌 게임은 두 명이서 즐기는 재밌는 게임이다.
탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.
두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.
"""
# 1. 처음 생각한 방법
N = int(input())

if N % 2:
    print("SK")
else:
    print("CY")


# 2. 한줄코딩
print("SK" if int(input())%2 else "CY")


# 3. DP 1: 이 문제에서 사용 가능한 방법
N-1 N-3 --> 상대방 이겨
N-2 N-4 --> 내가 이겨

N = int(input())
winner = ["" for _ in range(N+1)]
winner[0] = "CY"
winner[1] = "SK"

if N >= 2:
    for i in range(2, N+1):
        winner[i] = winner[i-2]
print(winner[N])


# 3개 6개
0
3 --> SK
6 --> SK | CY




# 4. DP 2: 가져갈 수 있는 돌의 갯수가 바뀌어도 확장성 있게 사용 가능한 방법
N = int(input())

if N == 1 or N == 3:
    print("SK")
elif N == 2 or N == 4:
    print("CY")
else:
    winners = [set() for _ in range(N+1)]
    winners[1] = winners[3] = {"SK"}
    winners[2] = winners[4] = {"CY"}
    for i in range(5, N+1):
        # union - 합집합
        winners[i] = winners[i-2] | winners[i-4]
    for i in winners[N]:
        print(i)