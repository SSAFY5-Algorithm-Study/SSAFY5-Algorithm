def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    last_cam = routes[0][1]
    for route in routes[1:]:
        if route[0] > last_cam:
            last_cam = route[1]
            answer += 1
    return answer