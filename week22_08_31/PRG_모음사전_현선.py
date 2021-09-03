# A, AA, AAA, AAAA, AAAAA, AAAAE, AAAAI, ....
# A가 젤 앞이고, 5개가 되는 경우의 수 : 5 X 5 X 5 X 5 = 625
# A가 젤 앞이고, 4개가 되는 경우의 수 : 5 X 5 X 5 = 125
# A가 젤 앞이고, 3게가 되는 경우의 수 : 5 X 5 = 25
# A가 젤 앞이고, 2개가 되는 경우의 수 : 5
# A가 젤 앞이고, 1개가 되는 경우의 수 : 1
# 총 781
# A - E 사이의 간격 : 781
# A : 1, E: 1+781 = 782, I: 782 + 781= 1563

# 재귀로도 풀 수 있을듯.
def solution(word):
    x = 781
    answer = 0
    
    alphabets = ['A','E','I','O','U']
    

    # word = 'AAAAA' -> 5
    # word = 'AAAAE' -> 6
    # word = 'AAAAI' -> 7
    # word = 'AAAAO' -> 8
    # word = 'AAAAU' -> 9
    # 1차이
    
    # word = 'AAAA' -> 4
    # word = 'AAAE' -> 10
    # word = 'AAAI' -> 16
    # word = 'AAAO' -> 22
    # word = 'AAAU' -> 28
    # 6차이
    
    # word = 'AAA' -> 3
    # word = 'AAE' -> 34
    # word = 'AAI' -> 65
    # word = 'AAO' -> 96
    # word = 'AAU' -> 127
    # 31 차이
    
    # word = 'AA'  -> 2
    # word = 'AE' -> 158
    # word = 'AI' -> 314
    # word = 'AO' -> 470
    # word = 'AU' -> 626
    # 156 차이
    
    # word = 'A' -> 1
    # word = 'E' -> 786
    # word = 'I' -> 1563
    # word = 'O' -> 2344
    # word = 'U' -> 3125
    # 785 차이
    
    for i in range(len(word)):
        for j in range(5):
            if alphabets[j] == word[i]:
                answer += j * x + 1
                break
        # 한 글자 뒤로 갈 때마다 경우의 수는 5배씩 떨어짐.
        if x > 0:   
            x = (x-1) // 5
        # 780 -> 156 -> 31 -> 6 -> 1
    print(answer)
    
    return answer