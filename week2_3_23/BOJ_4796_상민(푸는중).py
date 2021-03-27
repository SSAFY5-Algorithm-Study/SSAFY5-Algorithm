while
    L, P, V = map(int,input().split())


    ans = 0
    share, remainder = divmod(V, P)
    ans += share * L
    if remainder > L:
        ans += L
    ans += remainder