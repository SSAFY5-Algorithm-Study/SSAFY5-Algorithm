A, B = input(), input()
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
arr = []

for i in range(len(A)):
    arr += [alpha[ord(A[i]) - ord("A")], alpha[ord(B[i]) - ord("A")]]

while len(arr) > 2:
    for i in range(0, len(arr)-1):
        arr[i] = (arr[i] + arr[i+1]) % 10
    arr.pop()

print(''.join(map(str, arr)))
