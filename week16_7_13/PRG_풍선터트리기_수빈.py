# 풍선이 살아남는 경우 : 내 양 옆 중 하나가 나보다 크기가 클 때
# 풍선이 터뜨려지는 경우 : 내 양 옆 모두가 나보다 작을 때

# a     : -16  27  65  -2  58 -92 -71 -68 -61 -33
# left  : -16 -16 -16 -16 -16 -92 -92 -92 -92 -92
# right : -92 -92 -92 -92 -92 -92 -71 -68 -61 -33

INF = 10e9 + 1
def solution(a):
    answer = 0
    length = len(a)
    left, right = [INF] * length, [INF] * length
    left[0] = a[0]
    right[-1] = a[-1]
    
    # 왼쪽부터 시작해서 최솟값 저장
    for i in range(1, length):
        left[i] = min(left[i-1], a[i])
        
    # 오른쪽부터 시작해서 최솟값 저장
    for i in range(length-2, -1, -1):
        right[i] = min(right[i+1], a[i])
    
    # 해당 인덱스의 왼쪽, 오른쪽 최솟값이 a[i]보다 작으면 살아남지 X
    for i in range(length):
        if left[i] < a[i] and right[i] < a[i]:
            answer += 1
    
    return length - answer