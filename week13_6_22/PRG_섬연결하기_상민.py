def find_set(x, p):
    while x != p[x]:
        x = p[x]
    return x


def solution(n, costs):
    costs_sorted = sorted(costs, key=lambda x: x[2])
    p = [i for i in range(n)]
    answer = 0
    for s, e, w in costs_sorted:
        res_s, res_e = find_set(s, p), find_set(e, p)
        # 싸이클이 형성되지 않는 요소에서만 union 진행
        if res_s != res_e:
            p[res_e] = res_s
            answer += w
    return answer