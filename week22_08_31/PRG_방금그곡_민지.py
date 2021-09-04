notes_dict = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}

def replace_notes(notes):
    for k, v in notes_dict.items():
        notes = notes.replace(k, v)
    return notes

def solution(m, musicinfos):
    answer = '(None)'
    m = replace_notes(m)
    max_duration = 0
    
    # 각 음악 정보 가공하기
    for info in musicinfos:
        start_time, end_time, title, notes = info.split(",")
        
        # 1. 총 몇초간 재생됐는지 구하기
        ## 시간 계산을 위해 분으로 변환
        start_time = int(start_time[0:2]) * 60 + int(start_time[3:5])
        end_time = int(end_time[0:2]) * 60 + int(end_time[3:5])

        ## 총 재생 시간
        duration = end_time - start_time
        
        # 2. 악보에 있는 C#, D#, F#, G#, A# 처리하기
        ## 예시: C# --> c 로 치환해서 사용
        ## notes_dict 안에 있는 key들을 value로 바꿔서 사용
        notes = replace_notes(notes)
    
        # 3. 총 재생된 길이에 맞춰서 악보를 늘리거나 줄이기
        ## 예시: notes = "ABC", duration = 6 --> played = "ABCABC"
        ## rep = 전체 반복 재생 횟수, remainder = 나머지
        rep, remainder = divmod(duration, len(notes))
        played = notes * rep + notes[:remainder]
        
        # 4. 들은 부분이 재생된 음악에 있는지 체크하기
        # 부분이 일치하고, 동률일 경우 재생시간이 max라면 해당 곡의 정보 저장
        if m in played and duration > max_duration:
            answer = title
            max_duration = duration
    
    return answer