def solution(dartResult):
    # 점수를 담아둘 리스트
    shots = []
    idx = -1
    value = ''
    for dart in dartResult:
        if dart.isdigit():
            value += dart
            continue
        if value:
            shots.append(int(value))
            idx += 1
        if dart == 'S':
            shots[idx] **= 1
        elif dart == 'D':
            shots[idx] **= 2
        elif dart == 'T':
            shots[idx] **= 3
        elif dart == '*':
            if idx:
                shots[idx - 1] *= 2
            shots[idx] *= 2
        elif dart == '#':
            shots[idx] *= -1
        value = ''

    return sum(shots)