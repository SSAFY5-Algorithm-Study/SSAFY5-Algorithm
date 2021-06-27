def solution(n, costs):
    
    def find_set(x):
        if x != parent[x]:
            parent[x] = find_set(parent[x])
        return parent[x]
    
    costs.sort(key=lambda x: x[2])
    parent = list(range(n))
    count, cost = 0, 0
    for s, e, w in costs:
        s_root, e_root = find_set(s), find_set(e)
        if s_root != e_root:
            parent[e_root] = s_root
            cost += w
            count += 1
            if count >= n-1:
                break
    return cost