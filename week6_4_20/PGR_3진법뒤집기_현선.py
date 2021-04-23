



# 접근 : 소인수 분해해서, 몫은 다시 3으로 나눠주고, 나머지는 문자열에 더해주면 10진수를 3진수로 바꾼 거꾸로가 됨
# 그놈을 10진수로 변환.

def solution(n):
    three = ''
    # 소인수 분해하기
    while n != 0:
        mok = n // 3
        namerge = n % 3
        three += str(namerge)
        n = mok
    answer = int(three, 3)
    return answer