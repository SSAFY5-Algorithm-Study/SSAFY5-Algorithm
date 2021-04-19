N = int(input())
buildings = list(map(int, input().split()))
high1, high2 = sorted(set(buildings), reverse=True)[:2]
print(high1, high2)
