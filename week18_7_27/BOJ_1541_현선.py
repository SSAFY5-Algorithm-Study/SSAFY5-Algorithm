'''
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.
  입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.

'''


# input_sick = input()

# sick = []

# s = ''
# for i in range(len(input_sick)):
#     if input_sick[i] == '-' or input_sick[i] == '+':
#         sick.append(int(s))
#         sick.append(input_sick[i])
#         s = ''
#     else:
#         s += input_sick[i]
# sick.append(s)
# print(sick)
        

# 이러면 마이너스 기준으로 분류됨
input_sick = input().split('-')

total = 0
# 첫번째 값은 걍 다 더해짐
sick = input_sick[0].split('+')
for num in sick:
    total += int(num)

# 이후 마이너스로 분류된 식들. 그놈들을 다 빼주면 최소값들일것.
# 괄호 앞에 마이너스가 붙으면 안의 플러스는 마이너스가 되니까.
sick = input_sick[1:]
for eachSick in sick:
    nums = eachSick.split('+')
    for num in nums:
        total -= int(num)

print(total)