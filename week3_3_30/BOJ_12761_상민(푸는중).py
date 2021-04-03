import sys
sys.stdin = open('input.txt')

def BFS(N, cnt):
    queue = [(N, cnt)]
    while queue:
        position = queue.pop(0)
        for calc, num in ways:
            cnt += 1
            if calc == '-':
                next_position = 0 if position - num <= 0 else position - num
                queue.append((next_position, cnt))
            elif calc == '+':
                next_position = position + num
                queue.append((next_position, cnt))
            elif calc == '*':
                next_position = position * num
                queue.append((next_position, cnt))

T = int(input())
for tc in range(1, T + 1):
    A, B, N, M = map(int, input().split())
    ways = [('-', 1), ('+', 1), ('+', A), ('-', A), ('+', B), ('-', B), ('*' + A), ('*' + B)]
    discovered = []
    cnt = 0
    BFS(N, cnt)
