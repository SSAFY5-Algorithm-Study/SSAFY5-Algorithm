N = int(input())

def find_level(s, e, level):
    if s == e:
        city[level].append(order[s])
    else:    
        mid = (s+e) // 2
        # print("mid: ", mid, "level: ", level, s, e)
        city[level].append(order[mid])
        find_level(s, mid-1, level+1)
        find_level(mid+1, e, level+1)

city = [[] for _ in range(N)]
order = list(map(int, input().split()))
find_level(0, len(order)-1, 0)

for level in city:
    print(" ".join(map(str, level)))