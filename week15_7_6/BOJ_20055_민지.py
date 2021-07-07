"""
접근법
1. 내구도를 담은 배열과 로봇의 위치를 담은 배열 두개를 만들어서 기록하자
2. 디버깅 할때 편하게 각 과정을 함수화 시켜서 만들자
"""
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

# 1. 벨트 회전
def move_belt():
    belt.rotate(1)
    robots.rotate(1)
    s = (s+1) % (2*N)
    # 벨트 이동 후 내리는 자리에 있는 로봇이 있다면 내린다
    if robots[N-1]:
        robots[N-1] = 0

# 2. 로봇 이동
def move_robots(s):
    for r in range(2*N):


N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0] * (2*N))
robots[-1] = 2
s = 0

