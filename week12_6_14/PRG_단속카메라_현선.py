def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[0])
    camera_point = routes[0][1]
    # print(routes)
    for route in routes[1:]:
        if route[0] <= camera_point:
            camera_point = min(route[1], camera_point)
        else:
            camera_point = route[1]
            answer += 1
        # print(camera_point)
    # print(answer)
    return answer + 1