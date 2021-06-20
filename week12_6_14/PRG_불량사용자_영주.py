# 2019 카카오 개발자 겨울 인턴십: 불량 사용자

import re


def get_matching_groups(user_id, banned_id):
    groups = [[] for _ in range(len(banned_id))]
    for i, ban in enumerate(banned_id):
        ban_regex = re.compile(ban.replace('*', '\w'))
        for user in user_id:
            if len(ban) == len(user) and ban_regex.match(user):
                groups[i].append(user)
    return groups


def solution(user_id, banned_id):

    def find_cases(depth, case):
        if depth >= len(banned_id):
            cases.add(tuple(sorted(case)))
            return
        for matched_word in groups[depth]:
            if matched_word not in case:
                find_cases(depth+1, case+[matched_word])

    groups = get_matching_groups(user_id, banned_id)
    cases = set()
    find_cases(0, [])
    return len(cases)
