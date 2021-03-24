tc = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    div, mod = divmod(V, P)
    mod = mod if mod <= L else L
    ans = div * L + mod
    print("Case %d: %d" % (tc, ans))
    tc += 1