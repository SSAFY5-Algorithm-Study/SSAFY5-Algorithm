'''
2669. 직사각형 네개의 합집합의 면적 구하기

평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 
이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.
이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.
'''
base = [[0] * 100 for _ in range(100)]

for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            base[i][j] += 1
        
area = 0
for i in range(100):
    for j in range(100):
        if base[i][j]:
            area += 1

print(area)

'''
[입력]
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6

[출력]
26
'''