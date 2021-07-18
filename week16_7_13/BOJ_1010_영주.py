# 1010. 다리 놓기 (실버5)

# 직접 구현
import sys
input = sys.stdin.readline

factorials = [1]
for i in range(1, 31):
    factorials.append(factorials[-1]*i)

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorials[m]//(factorials[n]*factorials[m-n]))
    

"""
# 라이브러리 사용

import sys
from math import factorial
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(n)*factorial(m-n)))
"""
