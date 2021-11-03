T = int(input())

concats = [
    lambda x, y: (str(x) + ' ' + str(y)),
    lambda x, y: (str(x) + '+' + str(y)),
    lambda x, y: (str(x) + '-' + str(y))
]

ops_dict = {
    '+': lambda x, y: (x + y),
    '-': lambda x, y: (x - y)
    }

def evaluate(eq):
    eq = eq.replace(' ', '')
    result = 0
    num = ''
    sign = '+'

    for i in eq:
        if i.isdigit():
            num += i
        else:
            result = ops_dict[sign](result, int(num))
            num = ''
            sign = i
    
    result = ops_dict[sign](result, int(num))
    return result
    

def make_zero(eq, num):
    if num == N+1:
        if not evaluate(eq):
            print(eq)
        return

    for concat in concats:
        new_eq = concat(eq, num)
        make_zero(new_eq, num+1)


for _ in range(T):
    global N
    N = int(input())
    # 1~N 까지의 리스트 생성
    nums = list(range(1, N+1))
    make_zero('1', 2)
    print("")