n,k = map(int, input().split())
# 입력 받고
arr = [list(map(int,input().split())) for _ in range(n)]
# 금메달, 은메달, 동메달 많은 순 정렬
arr.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)

result = 1
if arr[0][0] == k:
    print(result)
else:
    rank = 1
    for i in range(1, len(arr)):
        # k 나라를 찾았다면
        if arr[i][0] == k:
            # 이전 나라와 순위가 동일하다? 그럼 그냥 result에 rank 값 그대로.
            # 이전 나라와 순위가 다르다? 그럼 등수는 i+1등임.
            result = rank if (arr[i][1:] == arr[i-1][1:]) else (i+1)
            # result = (i+1) if arr[i][1:] != arr[i-1][1:] else result
            break
        # 중복 아니다? rank는 i+1 임.
        if arr[i][1:] != arr[i-1][1:]:
            rank = i + 1
    
    print(result)
