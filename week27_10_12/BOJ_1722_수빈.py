'''
1722. 순열의 순서

1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.
임의의 순열은 정렬을 할 수 있다. 예를 들어  N=3인 경우 {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}의 순서로 생각할 수 있다.
첫 번째 수가 작은 것이 순서상에서 앞서며, 첫 번째 수가 같으면 두 번째 수가 작은 것이, 두 번째 수도 같으면 세 번째 수가 작은 것이….
N이 주어지면, 아래의 두 소문제 중에 하나를 풀어야 한다. 
k가 주어지면 k번째 순열을 구하고, 임의의 순열이 주어지면 이 순열이 몇 번째 순열인지를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1≤N≤20)이 주어진다. 둘째 줄의 첫 번째 수는 소문제 번호이다. 
1인 경우 k(1≤k≤N!)를 입력받고, 2인 경우 임의의 순열을 나타내는 N개의 수를 입력받는다. 
N개의 수에는 1부터 N까지의 정수가 한 번씩만 나타난다.

출력
k번째 수열을 나타내는 N개의 수를 출력하거나, 몇 번째 수열인지를 출력하면 된다.
'''
# itertools 사용 -- 메모리 초과
# import sys
# from itertools import permutations as perm
# input = sys.stdin.readline

# N = int(input())
# nums = [str(i) for i in range(1, N+1)]
# question = list(map(int, input().split()))
# perms = list(map(list, perm(nums)))

# # k번째 순열 구하기
# if question[0] == 1:
#     print(' '.join(perms[question[1]-1]))
# # 주어진 순열이 몇번째 순열인지 구하기
# else:
#     p = list(map(str, question[1:]))
#     print(perms.index(p))


# 직접 구현 -- 시간 초과
# import sys
# input = sys.stdin.readline

# def first(arr, depth, k):
#     global cnt
#     print(cnt)
#     global flag
#     if flag:
#         return
#     # depth가 0부터 시작하여 N이라면 N개를 모두 뽑은 것
#     if depth == N:
#         cnt += 1
#         if cnt == k:
#             print(' '.join(map(str, arr)))
#             flag = 1
#             return
#         return
#     for i in range(depth, N):
#         # 각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고,
#         # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고,
#         # 원상복구 하여 다시 경우의 수를 찾는다
#         arr[i], arr[depth] = arr[depth], arr[i]
#         first(arr, depth+1, k)
#         arr[i], arr[depth] = arr[depth], arr[i]

# def second(arr, depth, k):
#     global cnt
#     print(cnt)
#     global flag
#     if flag:
#         return
#     if depth == N:
#         cnt += 1
#         if arr == k:
#             print(cnt)
#             flag = 1
#             return
#         return
#     for i in range(depth, N):
#         arr[i], arr[depth] = arr[depth], arr[i]
#         second(arr, depth+1, k)
#         arr[i], arr[depth] = arr[depth], arr[i]

# N = int(input())
# nums = [i for i in range(1, N+1)]
# selected = [False for _ in range(N)]
# question = list(map(int, input().split()))
# cnt = flag = 0

# # k번째 순열 구하기
# if question[0] == 1:
#     k = question[1]
#     first(nums, 0, k)
# # 주어진 순열이 몇번째 순열인지 구하기
# else:
#     k = question[1:]
#     second(nums, 0, k)

'''
[입력]
4
1 3

[출력]
1 3 2 4
'''