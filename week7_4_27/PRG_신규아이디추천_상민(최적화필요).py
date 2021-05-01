def solution(new_id):
    chars = list('-_.')
    # 단계별로 치환
    # 1단계
    new_id = new_id.lower()

    # 2단계
    second_level = ''
    for char in new_id:
        if char.isalpha() or char.isdigit():
            second_level += char
        elif char in chars:
            second_level += char
    # 3단계
    for _ in range(400):
        second_level = second_level.replace('..', '.').replace('..', '.')
    third_level = second_level
    # 4단계
    fourth_level = list(third_level)
    if fourth_level and fourth_level[0] == '.':
        fourth_level.pop(0)
    if fourth_level and fourth_level[-1] == '.':
        fourth_level.pop()

    # 5단계
    if not fourth_level:
        fourth_level.append('a')

    # 6단계
    if len(fourth_level) >= 16:
        sixth_level = fourth_level[:15]
        if sixth_level[-1] == '.':
            sixth_level.pop()
    else:
        sixth_level = fourth_level

    # 7단계
    while len(sixth_level) <= 2:
        sixth_level.append(sixth_level[-1])

    return ''.join(map(str, sixth_level))