# 크러스컬로 가자.
# def solution(n, costs):
#     def find_daepyo(x):
#         while daepyo[x] != x:
#             x = daepyo[x]
#         return x
    
#     answer = 0
#     costs.sort(key=lambda x:x[2])
#     daepyo = list(range(n))
#     cnt = 0
#     i = 0
#     while cnt < n and i < len(costs):
#         temp = costs[i]
#         if find_daepyo(temp[0]) != find_daepyo(temp[1]):
#             answer += temp[2]
#             daepyo[find_daepyo(temp[0])] = find_daepyo(temp[1])
#             cnt += 1
#             i += 1
#         else:
#             i += 1
#     return answer


# 크러스컬로 가자.
def solution(n, costs):
    def find_daepyo(x):
        if x != daepyo[x]:
            daepyo[x] = find_daepyo(daepyo[x])
        return daepyo[x]
    
    answer = 0
    costs.sort(key=lambda x:x[2])
    daepyo = list(range(n))
    cnt = 0
    i = 0
    while cnt < n and i < len(costs):
        temp = costs[i]
        daepyo1 = find_daepyo(temp[0])
        daepyo2 = find_daepyo(temp[1])
        if daepyo1 != daepyo2:
            daepyo[daepyo2] = daepyo1
            answer += temp[2]
            cnt += 1
            i += 1
        else:
            i += 1
    return answer