'''
<아이디어>
정해진 skill의 순서에 맞게 skill을 찍는 것이 중요한 부분
'순서'에 집중을 해서 유저의 skill tree가 순서에 맞게 찍히는 지를 확인해줘야함
정해진 skill의 순서만 신경써주면 되기 때문에, 이외 skill들은 무시가능
-> 유저의 skill tree에서 하나씩 꺼내서, 선행 스킬 룰을 지켜야하는 지 파악해서
-> 현재 유저의 선행 스킬 현황과 비교해서 가능한지 불가능한지를 판단


'''


def solution(skill, skill_trees):
    # 정답 초기화
    answer = 0
    # skill_trees 배열 요소 하나하나 꺼내주기
    for skill_tree in skill_trees:
        # 스킬트리 순서가 맞게 진행되는 지 표시해주는 idx
        idx = 0
        # 각 스킬트리에서 스킬 하나하나 꺼내서
        for skill_element in skill_tree:
            # 정해진 스킬트리 룰에 존재하는 스킬인지 파악
            if skill_element in skill:
                # 존재한다면, 현재 유저의 선행스킬 현황과 비교해서 가능하다면
                if skill_element == skill[idx]:
                    # 스킬을 찍어주고, 스킬트리 순서 idx + 1
                    idx += 1
                    continue
                # 존재하지만, 선행스킬 순서를 지키지 않는다면, 불가능한 스킬트리!
                break
        # 선행스킬 순서에 다 맞게 유저가 스킬을 찍었다면
        else:
            # 정답 + 1
            answer += 1
    return answer
