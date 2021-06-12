'''
1<= n,m <= 100,000
'''


# 접근 : 딕셔너리 저장해서, 알파벳 입력이면 숫자 출력을, 아니면 포켓몬 이름을 출력하도록 한다.
n,m = map(int, input().split())
dogam = [input() for _ in range(n)]
dogam_dic = {i+1:j for i,j in enumerate(dogam)}
dogam_dic_two = {j:i+1 for i,j in enumerate(dogam)}
for i in range(m):
    search = input()
    if search.isalpha():
        print(dogam_dic_two[search])
    else:
        print(dogam_dic[int(search)])
