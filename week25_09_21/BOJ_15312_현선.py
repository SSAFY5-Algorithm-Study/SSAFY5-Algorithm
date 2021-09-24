alpha = {'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':2, 'H':3, 'I':3, 
        'J':2, 'K':2, 'L':1, 'M':2, 'N':2, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1}
jongmin = input()
her = input()
namelen = len(her)
dp = [[0] * (namelen * 2) for _ in range(namelen * 2 - 1)]

i = 0
j = 0
while j < namelen:
    dp[0][i] = alpha[jongmin[j]]
    dp[0][i+1] = alpha[her[j]]
    i += 2
    j += 1

for i in range(1, len(dp)):
    for j in range(namelen*2 - i):
        hab = dp[i-1][j] + dp[i-1][j+1]
        if hab > 10:
            hab -= 10
        dp[i][j] = hab

print(str(dp[-1][0]) + str(dp[-1][1]))