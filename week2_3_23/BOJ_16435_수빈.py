'''
16435. 스네이크버드

스네이크버드는 뱀과 새의 모습을 닮은 귀여운 생물체입니다. 
스네이크버드의 주요 먹이는 과일이며 과일 하나를 먹으면 길이가 1만큼 늘어납니다.
과일들은 지상으로부터 일정 높이를 두고 떨어져 있으며 i (1 ≤ i ≤ N) 번째 과일의 높이는 hi입니다. 
스네이크버드는 자신의 길이보다 작거나 같은 높이에 있는 과일들을 먹을 수 있습니다.
스네이크버드의 처음 길이가 L일때 과일들을 먹어 늘릴 수 있는 최대 길이를 구하세요.
'''
# 과일의 개수 N, 스네이크 버드 초기 길이 snake_length
N, snake_length = map(int, input().split())
# 과일이 있는 높이
fruits = list(map(int, input().split()))
# 낮은 곳에 달린 과일부터 비교하기 위해 정렬
fruits.sort()
# 과일 하나씩 비교해서 스네이크버드의 길이가 과일의 높이보다 작거나 같으면 1씩 증가
for fruit in fruits:
    if snake_length < fruit:
        continue
    snake_length += 1

print(snake_length)
'''
[입력]
3 10
10 11 13

[출력]
12
'''