import itertools

def solution(orders, course):
    answer = []
    # 만들 수 있는 코스 메뉴별 개수 count  
    course_menu = {}
    for num in course:
        course_menu[num] = {}
        for order in orders:
            # sorted(order) 안 하면 WX, XW 와 같은 경우를 다르게 인식함
            for menu in itertools.combinations(sorted(order), num):
                course_menu[num][menu] = course_menu[num].get(menu, 0) + 1
    # 메뉴 개수 내림차순 정렬하고 추가
    for num in course:
        # 정렬한 것 중 첫 요소가 2 이상이면 그 값이랑 개수 같은 것들 추가
        menu_count = 2
        # print(sorted(course_menu.get(num).items(), key=lambda x:x[1], reverse=True))
        for menu in sorted(course_menu.get(num).items(), key=lambda x:x[1], reverse=True):
            if menu[1] >= menu_count:
                answer.append(''.join(menu[0]))
                menu_count = menu[1]
            else:
                break
        
    return sorted(answer)