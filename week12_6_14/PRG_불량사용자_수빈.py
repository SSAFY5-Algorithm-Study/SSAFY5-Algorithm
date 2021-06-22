from itertools import permutations

def is_ban(user, banned):
    for i in range(len(banned)):
        length = len(banned[i])
        # 길이가 다르면 무조건 해당 안됨
        if len(user[i]) != length:
            return False
        # 마스킹된 곳 제외하고 동일한지 여부 비교
        for j in range(length):
            if banned[i][j] == '*':
                continue
            if banned[i][j] != user[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    banned_list = []
    
    # 가능한 경우 다 구해서 체크..? 
    user_perm = list(permutations(user_id, len(banned_id)))
    
    for user in user_perm:
        if is_ban(user, banned_id):
            # 목록 내용 동일하면 같은 것 -- set 처리
            user = set(user)
            if user not in banned_list:
                banned_list.append(user) 
            
    return len(banned_list)