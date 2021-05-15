'''
문제
평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 
이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 
변이나 꼭짓점이 겹칠 수도 있다.

이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

입력
입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다. 
첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 
세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 
모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

출력
첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.
'''

# 입력 : 왼쪽 아래 x,y  오른쪽 위 x,y
# 접근 : 모든 x좌표, y좌표는 1이상 100이하라고 했으므로, 그냥 2차원 좌표 배열을 만들어서, 범위 체크
# 좌표에 이미 1이 들어가 있으면 겹치니까, 겹치는 카운트 추가.


jwapyo = [[0] * 100 for _ in range(101)]
# 각 사각형의 넓이가 더해짐. (일단 겹치는거 신경안쓰고)
area = 0
total_gyupchim = 0
for _ in range(4):
    left_x, left_y, right_x, right_y = map(int, input().split())
    area += (right_x-left_x) * (right_y-left_y)
    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            # 이미 좌표에 1이 있으면 겹치니까 겹치는 카운트 추가.
            if jwapyo[i][j]:
                total_gyupchim += 1
            # 아니면 1로 채움.
            else:
                jwapyo[i][j] = 1
print(area-total_gyupchim)