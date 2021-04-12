def solution(n, arr1, arr2):
    bin_arr1 = []
    bin_arr2 = []
    secret_map = []
    
    for num in arr1:
        bin_arr1.append(bin(num)[2:].zfill(n))
    for num in arr2:
        bin_arr2.append(bin(num)[2:].zfill(n))
    
    for i in range(n):
        temp = ""
        for j in range(n):
            if int(bin_arr1[i][j]) | int(bin_arr2[i][j]):
                temp += "#"
            else:
                temp += " "
        secret_map.append(temp)
    
    return secret_map