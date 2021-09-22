def solution(enter, leave):
    length = len(enter)
    meet = [0] * length
    meeting_room = set()
    e = l = 0
    
    while e < length or l < length:
        if l < length and leave[l] in meeting_room:
            meeting_room.remove(leave[l])
            l += 1
        else:
            meet[enter[e]-1] += len(meeting_room)
            for p in meeting_room:
                meet[p-1] += 1
            meeting_room.add(enter[e])
            e += 1       
    return meet