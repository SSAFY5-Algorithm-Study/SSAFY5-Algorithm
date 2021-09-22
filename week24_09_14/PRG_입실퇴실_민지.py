"""
**문제 해결 포인트**
반드시 만나야 되는 사람을 구하려면, 어떤 사람이 나갈 수 있는 한 가장 빨리 나갔을때, 그래도 마주치는 사람이 몇명인지 구하자

"""
def solution(enter, leave):
    i = j = 0
    N = len(enter)
    
    room = set()
    answer = [0] * N
    
    while i < N or j < N:
        # 퇴실이 가능한지 먼저 체크
        # 나가려는 사람이 현재 방 안에 들어와 있다면 무조건 나가기
        if leave[j] in room:
            room.remove(leave[j])
            answer[leave[j]-1] += len(room)
            for person in room:
                answer[person-1] += 1
            j += 1
        # 나가려는 사람이 현재 방 안에 없다면, 다음 사람 입실
        else:
            room.add(enter[i])
            i += 1
    return answer