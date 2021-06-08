'''
아이디어
-> edges를 다 구하고 서로를 가리키는 선이 있으면 Cycle
'''


def get_ans():
    for i in range(1, N):
        print(i)
        for j in edges[i]:
            if i in edges[j]:
                return 'CYCLE'
    else:
        return 'NO CYCLE'


N = int(input())
# 입력 왜 이렇게 받기 힘들지.. 머리가 안돌아간다.
edges = [[] for _ in range(N + 1)]
for i in range(1, N):
    temp = int(input())
    temp_list = list(map(int, input().split()))
    for j in temp_list:
        if j != N:
            edges[i].append(j)
print(get_ans())





