'''
아이디어
- 임의의 두 집 사이에 경로가 항상 존재해야 하므로 모든 점을 이으면서 최솟값을 구할 수 있는
Kruskal 사용!

'''


def find_set(x):
    if x != p[x]:
        x = p[x]
    return x


def kruskal():
    result = 0
    for s, e, w in sorted(edges, key=lambda x: x[2]):
        res_s, res_e = find_set(s), find_set(e)
        print(res_s, res_e, w)
        if res_s != res_e:
            p[res_e] = res_s
            result += w
    return result



N, M = map(int, input().split())
edges = list(tuple(map(int, input().split())) for _ in range(M))

p = [i for i in range(N + 1)]
print(kruskal())