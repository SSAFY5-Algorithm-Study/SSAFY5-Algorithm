def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        temp = ''
        flag = True
        
        # 선행 스킬에 포함되는 스킬만 temp에 저장
        for alpha in s:
            if alpha in skill:
                temp += alpha
        
        # temp의 순서가 선행 스킬의 순서와 동일해야 되기 때문에
        # 다르다면 flag를 False로 바꿔준 후 반복문 빠져 나가기
        for idx, j in enumerate(temp):
            if j != skill[idx]:
                flag = False
                break
        
        # 선행스킬의 순서와 temp의 순서가 동일한 경우에만 +1
        if flag:
            answer += 1
    
    return answer