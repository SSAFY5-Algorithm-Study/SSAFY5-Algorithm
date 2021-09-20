def solution(enter, leave):
    answer = [0] * len(enter)
    
    meeting_room = set()
    # enter 순서
    i = 0
    # leave 순서
    j = 0
    # 입실이 끝나거나, 퇴실이 끝나거나 할때까지 반복
    while i < len(enter) or j < len(leave):
        # 만약에, 떠나려고 하는 사람이 미팅룸에 있다면
        # 미팅룸에 있는 사람들은, 그 떠나려고 하는 사람과 무조건 마주침.
        # 떠나려고 하는 사람은, 미팅룸에 남은 사람들 수만큼 마주침
        if leave[j] in meeting_room:
            # 미팅룸에 있다면, 떠나라!
            meeting_room.remove(leave[j])
            # 미팅룸에 남아있는 사람들은 떠난 사람과 마주쳤으므로 1씩 증가
            for k in meeting_room:
                answer[k-1] += 1
            # 떠난 사람은 미팅룸에 있는 사람들과 모두 마주침
            answer[leave[j]-1] += len(meeting_room)
            j += 1
        # 떠날려고 하는 사람이 회의실에 없다?
        # 추가먼저
        else:
            meeting_room.add(enter[i])
            i += 1
        # print(meeting_room)
        # print('--------')
    return answer