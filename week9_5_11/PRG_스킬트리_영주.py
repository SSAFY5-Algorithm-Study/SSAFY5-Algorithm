# Summer/Winter Coding(~2018) 스킬트리

def solution(skill, skill_trees):
    answer = 0
    set_skill = set(skill)
    for skill_tree in skill_trees:
        temp = ''.join(s for s in skill_tree if s in set_skill)
        if not temp or not skill.find(temp):
            answer += 1
    return answer
