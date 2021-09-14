def solution(s):
    all_set = '[' + s[1:-1] + ']'
    set_list = eval(all_set)
    # 원소 하나인 경우 처리하기 위해 빈 튜플 추가
    set_list.append(set())
    # 길이순 정렬
    set_list.sort(key = lambda x: len(x))
    
    answer = []
    for i in range(1, len(set_list)):
        # 차집합
        nums = set_list[i] - set_list[i-1]
        answer.append(nums.pop())
    return answer