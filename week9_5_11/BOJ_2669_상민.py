E, S, M = map(int, input().split())

count = 0

while True:
    count += 1
    E_cycle, S_cycle, M_cycle = count % 15, count % 28, count % 19
    E_result = E_cycle if E_cycle else 15
    S_result = S_cycle if S_cycle else 28
    M_result = M_cycle if M_cycle else 19

    if E == E_result and S == S_result and M == M_result:
        break

print(count)