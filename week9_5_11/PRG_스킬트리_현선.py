def solution(skill, skill_trees):
    # 접근 : 각각의 skill_tree에 skill이 몇개가 존재하는지 확인하고,
    # 순서를 체크하는 배열을 통해, 체크된 숫자와 skill이 존재하는 개수를 비교해 같으면 알맞는 스킬트리.
    # skill : 선행 스킬 순서
    # skill_trees : 스킬 트리를 담은 배열
    answer = 0
    checked = [0] * len(skill)
    
    # skill_trees에서 스킬트리를 하나씩 가져옴
    for skill_tree in skill_trees:
        
        # skill 문자열에 있는 알파벳들이 스킬트리에 몇개가 존재하는지 확인
        skill_cnt = 0
        for s in skill:
            if s in skill_tree:
                skill_cnt += 1
                
        # 스킬트리에서, 알파벳을 하나씩 가져와서 skill 문자열 순서 맞는지 체크.
        # checked라는 배열을 통해
        i = 0
        for s in skill_tree:
            if s == skill[i]:
                checked[i] = 1
                i += 1
                if i == skill_cnt:
                    break
        # checked 배열의 1의 개수가 skill_cnt와 같으면 순서가 맞는거니까, answer에 1 추가
        if checked.count(1) == skill_cnt:
            answer += 1
        #checked 배열은 초기화
        checked = [0] * len(skill)
    # 개 비효율적인듯.
    
    return answer