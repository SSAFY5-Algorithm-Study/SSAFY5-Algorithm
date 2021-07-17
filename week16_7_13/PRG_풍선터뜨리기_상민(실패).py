'''
아이디어 ->
- index로 조진다
- left_idx == -1 and right_idx == len(list)일때까지 while 반복
- left_idx가 -1이 되면 오른쪽으로만 가기
- 왼쪽부터 탐색
- 작은 것을 터뜨릴 수 있는 기회는 단 한번
- 이후에는 큰 것을 터뜨려야함
- flag 세워서 둘 다 통과못하면 break
'''

def solution(a):
    print(a)
    a_len = len(a)
    result = 0
    for i in range(a_len):
        left_idx = i - 1
        right_idx = i + 1
        chance = 1
        while True:
            print(i, left_idx, right_idx, a_len)
            if  left_idx == -1 and right_idx == a_len:
                print('들어와?')
                result += 1
                break
            # 왼쪽이랑 비교
            if left_idx >= 0:
                if a[left_idx] > a[i]:
                    left_idx -= 1
                    continue
                else:
                    if chance:
                        left_idx -= 1
                        chance -= 1
                        continue
                    # 더 이상 터뜨릴 수 없음
                    break
            # 오른쪽이랑 비교
            elif right_idx <= a_len - 1:
                if a[right_idx] > a[i]:
                    right_idx += 1
                    continue
                else:
                    if chance:
                        right_idx += 1
                        chance -= 1
                        continue
                    # 더 이상 불가
                    break
    return result


print(solution(list(map(int,input().split()))))
