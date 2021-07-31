import heapq

def solution(scoville, K):
    # 최소힙으로 변환
    heapq.heapify(scoville)
    # 섞은 횟수
    answer = 0
    # 가장 작은 스코빌 지수가 K 이상이 될 때까지 실행
    while scoville[0] < K:
        answer += 1
        # 가장 작은 스코빌 지수의 음식
        first = heapq.heappop(scoville)
        # 두번째로 작은 스코빌 지수의 음식
        second = heapq.heappop(scoville)
        # 두 음식 섞기
        mix = first + (second * 2)
        # 섞은 음식 다시 넣기
        heapq.heappush(scoville, mix)
        # 모든 음식을 섞은 후에도 스코빌 지수가 K 미만인 경우
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer