# 탐욕법(Greedy) : 단속카메라

def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = 1
    prev_end = routes[0][1]
    for start, end in routes[1:]:
        if start > prev_end:
            camera += 1
            prev_end = end
    return camera