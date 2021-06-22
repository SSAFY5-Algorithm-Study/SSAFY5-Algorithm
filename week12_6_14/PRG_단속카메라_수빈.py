def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera_cnt = 1
    out_camera = routes[0][1]
    for s, e in routes[1:]:
        if s > out_camera:
            camera_cnt += 1
            out_camera = e
    return camera_cnt