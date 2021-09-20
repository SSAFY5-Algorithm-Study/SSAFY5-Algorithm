def solution(weights, head2head):
    answer = []
    # 복서번호: [승률, 자신보다 무거운 복서 이긴 횟수, 자기 몸무게]
    boxer = { idx: [0, 0, weight] for idx, weight in enumerate(weights, start=1) }
    
    for idx, result in enumerate(head2head, start=1):
        # 대결횟수
        fight = 0
        for i, res in enumerate(result):
            # 붙어본적 없으면 대결횟수 증가
            if res != "N":
                fight += 1
            # 이기는 경우
            if res == "W":
                boxer[idx][0] += 1
                # 자신보다 무거운 복서 이겼는지 확인
                if weights[idx-1] < weights[i]:
                    boxer[idx][1] += 1
        # 대결횟수와 이긴횟수 모두 구했으니 승률로 바꿔줌
        if fight:
            boxer[idx][0] = boxer[idx][0] / fight * 100
        else:
            boxer[idx][0] = 0
    
    # 조건에 맞도록 정렬
    play_result = sorted(boxer.items(), key=lambda x:(x[1], -x[0]), reverse=True)
    answer = [final[0] for final in play_result]
    return answer