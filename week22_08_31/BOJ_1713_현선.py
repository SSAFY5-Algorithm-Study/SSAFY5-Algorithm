n = int(input())
total_recommend = int(input())
recommended_student = list(map(int,input().split()))
picture_frame = []
cnt = []

i = 0
while i < total_recommend:
    # 이미 추천받은 학생인 경우
    if recommended_student[i] in picture_frame:
        index = picture_frame.index(recommended_student[i])
        cnt[index] += 1
    # 처음 추천 받는 학생의 경우
    else:
        # 만약 이미 사진틀이 가득 찼다면
        if len(picture_frame) == n:
            min_recommended_student = min(cnt)
            index = cnt.index(min_recommended_student)
            picture_frame.pop(index)
            cnt.pop(index)
            picture_frame.append(recommended_student[i])
            cnt.append(1)
        # 아직 안찼다면
        else:
            picture_frame.append(recommended_student[i])
            cnt.append(1)
    i += 1
picture_frame.sort()
print(*picture_frame)