"""
BOJ 1541 잃어버린 괄호

세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

예제:
입력: 55-50+40
출력: -35
"""
"""
접근방법:
현재 숫자 이전에 한번이라도 -가 나온적이 있으면, 괄호를 사용해서 그 숫자는 뺄샘을 할 수 있다

예제:
10- (1+2+3+4) -5
1+2-(3+4)-(5+6)-7

현재 숫자 이전에 빼기가 나온적이 있는지 없는지를 체크하는 sign이라는 변수를 만든다
나온적 없음 --> 1
나온적 있음 --> -1
현재 숫자 * sign을 계산해 total에 더해준다
"""
equation = input()

total = 0
idx = 0
num = ""
sign = 1

while idx < len(equation):
    current_val = equation[idx]
    if current_val.isdigit():
        num += current_val
    else:
        total += int(num) * sign
        num = ""
        if current_val == "-":
            sign = -1
    idx += 1

print(total + int(num) * sign)