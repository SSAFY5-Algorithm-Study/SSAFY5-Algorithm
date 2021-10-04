def solution(sizes):
    short = long = 0
    for size in sizes:
        a, b = sorted(size)
        short = a if a > short else short
        long = b if b > long else long
    return long * short