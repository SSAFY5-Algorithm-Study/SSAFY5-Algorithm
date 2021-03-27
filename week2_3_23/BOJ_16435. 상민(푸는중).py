N, L = map(int,input().split())
fruits = sorted([map(int,input().split())])

for fruit in fruits:
    if L <= fruit:
        L += 1
L
