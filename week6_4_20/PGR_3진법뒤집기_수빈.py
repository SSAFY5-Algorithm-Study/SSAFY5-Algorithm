'''
3진법 뒤집기

자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    t = ''
    # 자연수 n 3진수(역순)로 변환
    while n >= 1:
        n, r = divmod(n, 3)
        t += str(r)
    # 10진수로 변환
    answer = int(t, 3)
    return answer