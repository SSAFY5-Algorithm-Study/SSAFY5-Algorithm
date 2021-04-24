from itertools import combinations

def solution(orders, course):
    # 조합 담아줄 dict 생성
    menu_combination = {}
    answer = []
    # 메뉴 갯수별 조합 생성
    for num in course:
        # 메뉴 개수대로 dict내에 dict 또 생성 (dict가 hash형식이라서 처리가 list보다 더 빠름)
        menu_combination[num] = {}
        # 주문정보들에서 주문 정보 하나를 선택
        for order in orders:
            # 주문 정보 또한 오름차순으로 문자가 정렬되어 있어야 되기 때문에
            # 미리 sorted(문자열)을 통해서 정렬
            # 조합 라이브러리를 사용해서 원하는 메뉴 갯수대로 조합을 생성한 다음 요소 하나하나씩 선택
            for comb in combinations(sorted(order), num):
                # 해당 조합이 dict에 존재하면 
                if menu_combination[num].get(comb):
                    # 횟수 + 1
                    menu_combination[num][comb] += 1
                # 없으면
                else:
                    # 새로운 요소 생성 해주고 횟수 1로 초기화
                    menu_combination[num][comb] = 1
    for num in course:
        # 주문횟수가 2회 이상이어야해서 2회보다 작은 주문들은 처리되지 않게 설정
        max_value = 2
        if menu_combination.get(num):
            # 메뉴가 2,3,4개 인 것을 담고 있는 dict안 dict를 하나씩 선택해서
            # (('A', 'C'): 4) <- 이렇게 되어 있음
            # 여기서 메뉴가 존재하는 횟수를 기준으로 내림차순 정렬
            for temp in sorted(menu_combination.get(num).items(), key=lambda x:x[1], reverse=True):
                # 주문 횟수가 2회이상일 경우에만 확인
                if temp[1] >= max_value:
                    # 오름차순 정렬해놓았기 때문에 첫 요소는 무조건 정답에 추가
                    # 추가하면서 뒤의 요소들중에 첫 요소의 주문횟수와 같은 횟수가 있는 지 파악 하기 위해
                    # 값 저장
                    max_value = temp[1]
                    # ('A','B) 이런식으로 자료가 구성되어 있으니
                    # 'AB'를 만들어주고 정답 배열에 추가
                    answer.append("".join(map(str, temp[0])))
                # 주문 횟수가 2회 미만이거나
                # 현재 저장되어 있는 최대 주문 횟수보다 작으면
                else:
                    # 바로 for문 탈출 (내림차순으로 정렬되어 있기 때문에 뒤는 안봐도됨)
                    break
    return sorted(answer)


'''
1. dict안에 dict 생성
 - menu_combination = {}
 - menu_combination[num] = {}

2. sorted(문자열)
 - a~z순으로 정렬되어서 list형식으로 반환

3. 딕셔너리.get() 
 - 없으면 에러 안뜸
'''