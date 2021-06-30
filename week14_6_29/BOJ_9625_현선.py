k = int(input())
adp = [0] * 46
bdp = [0] * 46
adp[0] = 1
bdp[1] = 1

for i in range(2, k+1):
    adp[i] = bdp[i-1]
    bdp[i] = adp[i-1] + bdp[i-1]
print(adp[k], bdp[k])