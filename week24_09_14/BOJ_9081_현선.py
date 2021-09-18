from itertools import permutations

# product : 중복 순열 -> 모든 조합. 중복 허용.
# permutation : 순열
# combination : 조합 


n = int(input())

for _ in range(n):
    string = input()
    arr = permutations(string, len(string))
    answer = list(set(arr))
    result = []
    for i in range(len(answer)):
        result.append(''.join(answer[i]))
    result.sort()
    for index,st in enumerate(result):
        if st == string:
            break
    # print(index)
    dab = st if index == len(result)-1 else result[index+1]
    print(dab)
    