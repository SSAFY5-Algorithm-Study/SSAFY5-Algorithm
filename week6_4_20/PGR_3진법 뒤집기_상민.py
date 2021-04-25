def solution(n):
    ten_three = ''
    while n > 2:
        n, remainder = divmod(n, 3)
        ten_three += str(remainder)
    ten_three += str(n)
    return int(ten_three, 3)
