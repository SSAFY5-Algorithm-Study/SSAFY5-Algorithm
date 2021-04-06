def BFS(N, C):
    global M
    # 0 ~ 100000
    discovered = [0] * 100001
    queue = [(N, C)]
    while queue:
        current_position, cnt = queue.pop(0)
        # 8가지 방법으로 진행
        for calc, num in ways:
            # -
            if calc == '-':
                next_position = current_position - num
            # +
            elif calc == '+':
                next_position = current_position + num
            # *
            elif calc == '*':
                next_position = current_position * num
            # 다음 위치가 범위안에 존재하고 아직 발견되지 않았다면
            if 0 <= next_position <= 100000 and not discovered[next_position]:
                # 발견 표시
                discovered[next_position] = 1
                # 동규가 주미의 위치에 도착하는 것을 알았으면
                # cnt + 1 해주고
                if next_position == M:
                    # BFS 종료
                    return cnt + 1
                # queue에 (위치, count) 넣어줌
                queue.append((next_position, cnt + 1))


# T = int(input())
# for tc in range(1, T + 1):
A, B, N, M = map(int, input().split())
ways = [('-', 1), ('+', 1), ('+', A), ('-', A), ('+', B), ('-', B), ('*', A), ('*', B)]
print(BFS(N, 0))