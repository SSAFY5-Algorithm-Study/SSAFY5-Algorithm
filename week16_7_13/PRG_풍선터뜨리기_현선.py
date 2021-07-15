# 시간초과
def solution(a):
    # 풍선이 1개면 1반환
    if len(a) == 1:
        return 1
    # 풍선이 2개 이상인 경우
    # 처음과 끝 풍선은 살아남을 수 있음. 그러니까 answer을 2로 초기화 해놓고 진행.
    answer = 2
    for i in range(1,len(a)-1):
        if min(a[:i]) < a[i] and min(a[i:]) < a[i]:
            continue
        answer += 1
    return answer
    
# # 수정
# def solution(a):
#     # 풍선이 1개면 1반환
#     if len(a) == 1:
#         return 1
#     # 풍선이 2개 이상인 경우
#     # 처음과 끝 풍선은 무조건 살아남을 수 있음. 그러니까 answer을 2로 초기화 해놓고 진행.
#     answer = 2
#     minV = 1000000001
#     # 한 부분에서 왼쪽 최솟값들.
#     leftmin = [0] * len(a)
#     for i in range(len(a)):
#         if minV > a[i]:
#             minV = a[i]
#         leftmin[i] = minV
#     # print(leftmin)
#     # 최솟값 초기화
#     minV = 1000000001
#     # 한 부분에서 오른쪽 최솟값들.
#     rightmin = [0] * len(a)
#     for i in range(len(a)-1, -1,-1):
#         if minV > a[i]:
#             minV = a[i]
#         rightmin[i] = minV
#     for i in range(1, len(a)-1):
#         # 양쪽 최솟값 보다 크면 continue
#         if leftmin[i] < a[i] and rightmin[i] < a[i]:
#             continue
#         answer += 1
#     # print(rightmin)
#     return answer