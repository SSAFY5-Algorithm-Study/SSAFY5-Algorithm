'''
문제
세준시에는 고층 빌딩이 많다. 세준시의 서민 김지민은 가장 많은 고층 빌딩이 보이는 고층 빌딩을 찾으려고 한다. 
빌딩은 총 N개가 있는데, 빌딩은 선분으로 나타낸다. i번째 빌딩 (1부터 시작)은 (i,0)부터 (i,높이)의 선분으로 나타낼 수 있다. 
고층 빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 두 지붕을 잇는 선분이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다. 
가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 빌딩의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에 1번 빌딩부터 그 높이가 주어진다. 
높이는 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''
# 처음 접근 : 반복문 돌면서 현재 빌딩보다 낮은 빌딩 찾아가면서 개수 세기, 개수 세기에 포함된 낮은 빌딩보다 높은 빌딩 찾으면 stop
# 문제점 : 배열이 50개이기 때문에  


# 인터넷 풀이 참고.
# 기울기 : dy / dx

N = int(input())
buildings = list(map(int, input().split()))
see_buildings_count = [0] * N

for i in range(len(buildings)):
    max_gradient = -1000000000
    for j in range(i+1,N):
        # 현재 빌딩의 옥상 - 다음 빌딩들의 옥상 사이의 기울기 구하기
        current_gradient = (buildings[i] - buildings[j]) / (i - j)
        # 저장된 기울기 최대값 보다 작다? 그 빌딩은 못본다.
        # 기울기 최댓값 보다 크다면? 볼 수 있는 빌딩에 하나 추가해주고, 최대값 업데이트.
        if current_gradient > max_gradient:
            max_gradient = current_gradient
            # 볼 수 있는 빌딩 수 추가
            see_buildings_count[i] += 1
            # 지금 왼쪽에서 오른쪽으로만 탐색하고 있기 때문에, 현재 빌딩에서 왼쪽으로 볼 수 있는 빌딩들을 계산하면서 미리 추가해준다.
            see_buildings_count[j] += 1
print(max(see_buildings_count))