
# 실패
def solution(lines):
    if len(lines) == 1:
        return 1
    times = []
    for i in range(len(lines)):
        a,b,c = lines[i].split()
        h,m,s = b.split(':')
        sec = int(h) * 24 * 60 + int(m) * 60 + float(s)
        during = float(c[:-1])
        starttime = sec - during + 0.001
        if starttime < 0:
            starttime = 0
        times.append([starttime, sec])
    times.sort(key=lambda x:x[0])
    
    arr = [0] * 36720000
    for i in range(len(times)):
        s = int(times[i][0] * 1000)
        e = int(times[i][1] * 1000)
        arr[s:e] = [1] * (e-s)
    answer = max(arr)
    return answer