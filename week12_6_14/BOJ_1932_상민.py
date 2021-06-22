'''
아이디어
-> DP 문제이므로, [i][j + 0] [i][j + 1]로 최대 갱신
'''

N = int(input())
# 기존 숫자 배열
triangle = [list(map(int, input().split())) for _ in range(N)]
# 합한 숫자 배열
# 여러 번 합해지는 숫자가 존재하기 때문에 합해진 숫자 배열을 따로 만들어서 max 구함
triangle_sum = list([0] * i for i in range(1, N + 1))
# 배열의 [0][0]은 따로 더해주는 과정이 없으므로 초기 설정 필요
triangle_sum[0][0] = triangle[0][0]
triangle_length = len(triangle)
# 이중 리스트의 리스트 idx
for i in range(triangle_length - 1):
    # 내부 리스트의 요소 idx
    for j in range(len(triangle[i])):
        # 숫자마다 왼쪽 아래, 오른쪽 아래를 더해주면서 내려가기 때문에 
        # 기존에 합해진 숫자(존재하는 경우에만)와 이전까지의 숫자 + 기존 숫자를 비교하여 최대값을 저장
        triangle_sum[i+1][j] = max(triangle_sum[i+1][j], triangle[i+1][j] + triangle_sum[i][j])
        triangle_sum[i+1][j+1] = max(triangle_sum[i+1][j+1], triangle[i+1][j+1] + triangle_sum[i][j])
print(max(max(triangle_sum)))