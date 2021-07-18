import math

for _ in range(int(input())):
    w, e = map(int, input().split())
    print(math.factorial(e) // (math.factorial(w) * math.factorial(e - w)))
