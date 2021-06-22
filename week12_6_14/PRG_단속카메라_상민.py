'''
아이디어
-> 포함관계를 따지면서, 최소 대수를 구하자
-> 완전 탐색하면서, 범위를 설정
-> (a, b)라면 (a=더 큰수, b=더 작은 수)로 설정해주면서 현재 범위를 설정
-> 다음이 포함이 안되면, camera += 1, 범위 초기화
'''

def solution(routes):
    # 저번에 풀었던 정렬 문제와 비슷하게 접근
    routes.sort()
    # routes의 첫번째 요소를 현재 카메라 설치 범위로 할당
    area = routes[0]
    # 카메라 기본 설치 개수 1개
    camera = 1
    for idx in range(1, len(routes)):
        # 현재 카메라 범위안에 포함되어 있으면
        # ex) [-20, 15], [-14, -5]
        if area[1] >= routes[idx][0]:
            # 요소들을 모두 포함할 수 있는 카메라 범위 구하기
            # (더 큰 수, 더 작은 수)
            area = (max(area[0], routes[idx][0]), min(area[1], routes[idx][1]))
        # 현재 카메라 범위 밖의 요소가 등장하면
        else:
            # 카메라 설치
            camera += 1
            # 새로운 카메라 범위 설정
            area = routes[idx]

    return camera