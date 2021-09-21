# 문자를 숫자로, 숫자를 문자로 만들기 위한 dict 만드는 함수
def make_dict(value):
    idx = 0
    for i in sorted(value):
        if not word_dict.get(i):
            word_dict[i] = idx
            word_dict[idx] = i
            idx += 1

# 문자 -> 숫자, 숫자 -> 문자 함수
def change_format(word_value):
    temp = []
    for i in word_value:
        temp.append(word_dict.get(i))
    return temp

# 다음 단어를 찾아내는 함수
def get_next_word(original_word):
    # 1. 맨 뒤 2개 idx 비교해서 -2가 -1보다 작으면 서로 바꿔주고 다음 단어 반환
    if original_word[-1] > original_word[-2]:
        original_word[-1], original_word[-2] = original_word[-2], original_word[-1]
        return original_word
    # 2. 판가름이 나지않으면 그 다음 인덱스 탐색하여 바꿔준다.
    else:
        idx = -3
        while True:
            candidates = original_word[idx:]
            # 해당 인덱스가 나머지 숫자중에 제일 크면
            if original_word[idx] >= max(candidates):
                # 보다 더 앞에 인덱스 탐색
                idx += -1
                # 마지막 단어이면 기존 단어를 반환
                if abs(idx) == len(original_word) + 1:
                    return original_word
                continue
            # 더 크지 않으면
            else:
                sorted_candidates = sorted(candidates)
                # 기준 숫자의 마지막 인덱스 찾기
                last_index = max(index for index, item in enumerate(sorted_candidates) if item == original_word[idx])
                # 남은 숫자중에서 현재 인덱스보다 크면서 제일 작은 수(number)
                next_value = sorted_candidates[last_index + 1]                
                # 해당 숫자를 제거
                sorted_candidates.remove(next_value)
                # print(original_word[:idx], next_value, sorted(sorted_candidates))
                return original_word[:idx] + [next_value] + sorted(sorted_candidates)

                  
        

N = int(input())
for _ in range(N):
    w = input()
    word_dict = {}
    make_dict(w)
    word_numbered = change_format(w)
    next_word = get_next_word(word_numbered)
    print(''.join(change_format(next_word)))




