# leave 완전탐색
# leave 요소의 인덱스까지의 숫자들을 room 배열에 넣어주기 -> 각각 len(room) - 1만큼 result에 값입력
# leave 요소의 인덱스를 max_idx로 저장해놓음
# 다음 요소 탐색 -> 인덱스 가져오기 -> max_idx와의 사이의 elements들 room에 넣기 -> 기존에 있던 애들은 새로 추가된 애들을 더해주고 -> 새로 들어온 애들은 len(room) - 1을 해줌

def solution(enter, leave):
    room = []
    answer = [0] * (len(enter) + 1)
    # 추가할 요소들이 있는 지 없는 지 판단하는 변수
    max_idx = 0
    # leave 배열 완전 탐색
    for idx, leave_element in enumerate(leave):
        # 요소의 인덱스 저장
        temp_idx = enter.index(leave_element)
        # 새로 추가될 요소들 저장
        new_elements = enter[max_idx:temp_idx + 1]
        # 새로 추가될 요소들이 있다면
        if new_elements:
            # 현재 방에 요소가 있다면
            if room:
                # 방의 요소들에게 새로 추가될 요소들 더해주기
                for room_element in room:
                    answer[room_element] += len(new_elements)
            # 방에 새로 요소들 추가
            room += new_elements
            # 새로 추가된 요소들에게 만난 방 요소들 더해주기
            for new_element in new_elements:
                # 자기자신은 빼야하므로 -1
                answer[new_element] += len(room) - 1
        # 새로 추가될 요소들을 지정해주는 max_idx 업데이트
        max_idx = max(max_idx, temp_idx + 1)
        # 방에서 내보내기
        room.pop(room.index(leave_element))
    return answer[1:]
