N, L = map(int, input().split())
fruits = sorted(list(map(int, input().split())))

for fruit in fruits:
    if fruit <= L:
        L += 1
    else:
        break

print(L)
