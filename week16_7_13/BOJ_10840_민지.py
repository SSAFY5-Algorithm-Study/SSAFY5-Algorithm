def compare_hash(N):
    ans = 0
    # i에서부터 시작한 길이가 N인 문자열의 해시값 구하기
    # hash1 = 위치 해시값
    # hash2 = 값 해시값

    # 첫번째 str
    for i in range(0, len(str2)-N+1):
        hash1 = 1
        hash2 = 1
        for j in range(i, i+N):
            chr_idx = ord(str2[j]) - ord('a')
            num = primes[chr_idx]
            hash1 *= num
            hash1 %= mod
            hash2 *= primes[chr_idx + 26]
            hash2 %= mod
        hash_list[hash1].append((hash2, N))


    for i in range(0, len(str1)-N+1):
        hash1 = 1
        hash2 = 1
        for j in range(i, i+N):
            chr_idx = ord(str1[j]) - ord('a')
            num = primes[chr_idx]
            hash1 *= num
            hash1 %= mod
            hash2 *= primes[chr_idx + 26]
            hash2 %= mod
            
            # hash1 자리에 hash2의 값이 이미 들어있다면 --> 일치하는 문자열이 있다는 얘기
            for k in range(len(hash_list[hash1])):
                if(hash_list[hash1][k] == (hash2, N)):
                    return N



str1 = input()
str2 = input()
mod = 999979

primes = {}

idx = 0
# a~z, A~Z
for i in range(2,1000):
    flag = 1
    for j in range(2,int(i**0.5)):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        primes[idx] = i
        idx += 1


hash_list = [[] for _ in range(mod)]
    
N = min(len(str1), len(str2))

for i in range(N, 0, -1):
    ans = compare_hash(i)
    if ans != 0:
        break

print(ans)