def solution(m, musicinfos):
    answer = ''
    
    # 2글자 -> 1글자 처리
    if 'C#' in m:
        m = m.replace('C#', '1')
    if 'D#' in m:
        m = m.replace('D#', '2')
    if 'F#' in m:
        m = m.replace('F#', '3')
    if 'G#' in m:
        m = m.replace('G#', '4')
    if 'A#' in m:
        m = m.replace('A#', '5')
    
    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i].split(',')
        playTimeHour = int(musicinfo[1][:2]) - int(musicinfo[0][:2])
        playTimeMinute = int(musicinfo[1][3:]) - int(musicinfo[0][3:])
        if playTimeMinute < 0:
            playTimeHour -= 1
            playTimeMinute += 60
        playTime = playTimeMinute + playTimeHour * 60
        
        k = 0
        cnt = 0
        result = ''
        while cnt <= playTime:
            # musicinfo[3] = 코드 진행 (CDEFGAB...)
            # k가 musicinfo[3] 의 길이와 같아지면 0으로 초기화 (끝까지 가면 다시 처음부터 더해줌)
            if k == len(musicinfo[3]):
                k = 0
            # result에 playTime동안 계속 더해줌
            result += musicinfo[3][k]
            k += 1
            cnt += 1

        # 바까주기
        if 'C#' in result:
            result = result.replace('C#', '1')
        if 'D#' in result:
            result = result.replace('D#', '2')
        if 'F#' in result:
            result = result.replace('F#', '3')
        if 'G#' in result:
            result = result.replace('G#', '4')
        if 'A#' in result:
            result = result.replace('A#', '5')
        
        # 찾고자하는 코드가 result 안에 있으면 answer을 노래 제목으로.
        if m in result:
            answer = musicinfo[2]
            break
    return answer if answer else "(None)"