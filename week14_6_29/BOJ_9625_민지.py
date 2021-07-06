N = int(input())

a_cnt = 1
b_cnt = 0

for _ in range(N):
    temp_a = b_cnt
    temp_b = b_cnt + a_cnt
    a_cnt, b_cnt = temp_a, temp_b

print(a_cnt, b_cnt)