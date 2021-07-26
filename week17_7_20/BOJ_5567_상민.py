def checkNum():
    # visited = [0] * (n + 1)
    # answer = 0
    temp = set()
    if not AL[1]:
        return 0
    else:
        for one, another in relations:
            # and not visited[another]
            if one == 1:
                temp.add(another)
                for adj in AL[another]:
                    temp.add(adj)
        return len(temp) - 1
    
n = int(input())
m = int(input())
relations = []
AL = [[] for _ in range(n + 1)]
answer = 0

for _ in range(m):
    s, e = map(int, input().split())
    relations.append((s,e))
    AL[s].append(e)
    AL[e].append(s)
relations.sort()
print(checkNum())

