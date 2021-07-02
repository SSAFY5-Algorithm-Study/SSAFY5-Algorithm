# 90점. 효율성 만점.

def solution(s):
    answer = 0
    if len(s) == 1:
        return 1
    for i in range(len(s)-1):
        k = 1
        cnt = 1
        # 바로 뒤에꺼가 같을때
        if s[i] == s[i+1]:
            cnt = 2
            while (i-k > -1 and i+1+k < len(s)):
                if s[i-k] != s[i+1+k]:
                    break
                k += 1
                cnt += 2
        # 바로 뒤에꺼는 안같을때
        else:
            while (i - k > -1 and i + k < len(s)):
                if s[i-k] != s[i+k]:
                    break
                k += 1
                cnt += 2
        if answer < cnt: 
            answer = cnt
    return answer