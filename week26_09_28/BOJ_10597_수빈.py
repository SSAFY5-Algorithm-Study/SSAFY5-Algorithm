'''
10597. 순열장난

kriii는 1부터 N까지의 수로 이루어진 순열을 파일로 저장해 놓았다. 모든 수는 10진수로 이루어져 있고, 모두 공백으로 분리되어 있다.
그런데 sujin이 그 파일의 모든 공백을 지워버렸다!
kriii가 순열을 복구하도록 도와주자.

입력
첫 줄에 공백이 사라진 kriii의 수열이 주어진다.
kriii의 순열은 최소 1개 최대 50개의 수로 이루어져 있다.

출력
복구된 수열을 출력한다. 공백을 잊으면 안 된다.
복구한 수열의 경우가 여러 가지 일 경우, 그 중 하나를 출력한다.
'''
# 155987643211011121314 경우에 안 풀림
# import sys
# input = sys.stdin.readline

# num = input().strip()
# nums = [i for i in range(1, 51)]
# two = ''
# ans = []

# for n in num:
#     if two:
#         two += n
#         m = int(two)
#         if m in nums:
#             ans.append(two)
#             two = ''
#             nums.remove(m)
#     else:
#         m = int(n)
#         if m in nums:
#             ans.append(n)
#             two = ''
#             nums.remove(m)
#         else:
#             two += n

# print(' '.join(ans))

# N을 찾는 방법....?

'''
[입력]
4111109876532

[출력]
4 1 11 10 9 8 7 6 5 3 2
'''