'''
2023. 신기한 소수

수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.
7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 
수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.
수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

출력
N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.
'''
import math

# 시간복잡도 O(N)
# def is_prime(n):
#     num = int(n)
#     for i in range(2, num):
#         if not num % i:
#             return False
#     return True

# 시간복잡도 O(N^(1/2))
# 약수의 대칭성을 이용하면 x의 제곱근까지만 판별할 수 있다.
# 모든 약수는 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다.
# 따라서 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 된다.
# https://unounou.tistory.com/7 
# https://airvw.github.io/algorithm/2020-11-10-primenumber/
def is_prime(n):
    num = int(n)
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True

def dfs(n):
    if len(n) == N:
        print(n)
        return
    for num in next_num:
        if is_prime(n+num):
            dfs(n+num)

N = int(input())
# 첫번째 자리에 올 수 있는 수는 소수인 2, 3, 5, 7
first_num = ['2', '3', '5', '7']
# 그 이후 자리에 붙을 수 있는 숫자는 5가 아닌 홀수
next_num = ['1', '3', '7', '9']

for num in first_num:
    dfs(num)
'''
[입력]
4

[출력]
2333
2339
2393
2399
2939
3119
3137
3733
3739
3793
3797
5939
7193
7331
7333
7393
'''