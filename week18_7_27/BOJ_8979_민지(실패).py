N, K = map(int, input().split())

countries = [list(map(int, input().split()))[1:] for _ in range(N)]
key = countries[K-1]

countries.sort(reverse=True)
print(countries.index(key)+1)