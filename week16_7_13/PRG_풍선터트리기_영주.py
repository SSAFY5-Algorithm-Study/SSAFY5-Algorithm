# 월간 코드 챌린지 시즌1 : 풍선 터트리기

# 0번째 인덱스부터 시작해서, 각 인덱스까지의 최소값의 모임을 반환
def get_min_array(a):
    min_array = []
    min_value = a[0]
    for balloon in a:
        min_value = min(min_value, balloon)
        min_array.append(min_value)
    return min_array


def solution(a):
    answer = 0
    left = get_min_array(a) # 왼쪽 풍선 중 최소값 찾기
    right = get_min_array(a[::-1])[::-1] # 오른쪽 풍선 중 최소값 찾기
    for i in range(len(a)):
        if (left[i] >= a[i]) or (right[i] >= a[i]):
            answer += 1 # 왼쪽 최소값, 오른쪽 최소값 중 하나라도 기준 풍선보다 크거나 같으면 카운트
    return answer
