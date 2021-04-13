# BOJ 1094 막대기
# 최대한 짧게 만드는것을 목표로 풀었다
X = int(input())
print(sum([1 if X&(1<<i) else 0 for i in range(7)]))