def find_set(element):
    while element != p[element]:
        element = p[element]
    return element


def kruskal():
    # 모든 노드가 연결된지 count 해줄 수 있는 변수 초기화
    count = 0
    # 비용 변수 초기화
    cost = 0
    for s, e, w in edges:
        # 탈출
        if count == N:
            return cost
        # 이 노선의 노드들을 연결을 하면 싸이클이 생성되지 않으면
        fs, fe = find_set(s), find_set(e)
        if fe != fe:
            count += 1
            cost += w
            p[fe] = p[fs]
    return cost


N = int(input())
M = int(input())
info = [list(map(int, input().split())) for _ in range(M)]
edges = sorted(info, key=lambda x: x[2])
# 자신이 누굴 가리키고 있는 지 표시하는 배열
p = [i for i in range(N + 1)]
# 함수 호출
print(kruskal())

