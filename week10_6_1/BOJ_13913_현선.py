'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
'''

# 접근 : BFS로 풀면 될 듯.
# 근데, 경로를 다 알아야하니까, 배열 2개 써야할듯

def bfs(n):
    visit[n] = 0
    q.append(n)
    while q:
        temp = q.pop(0)
        if temp == K:
            return
        elif  0 <= temp-1 <= 100000 and visit[temp-1] == 0:
            q.append(temp-1)
            arr[temp-1] = temp
            visit[temp-1] = visit[temp] + 1
        elif 0 <= temp+1 <= 100000 and visit[temp+1] == 0:
            q.append(temp+1)
            arr[temp+1] = temp
            visit[temp+1] = visit[temp] + 1
        elif 0 <= temp * 2 <= 100000 and visit[temp*2] == 0:
            q.append(temp*2)
            arr[temp*2] = temp
            visit[temp*2] = visit[temp] + 1


N, K = map(int, input().split())
visit = [0] * 100001
arr = [0] * 100001
q = []
# bfs 돌리고
bfs(N)
# 몇번 이동했는지 출력하고
print(visit[K])
# 역으로 거슬러 올라가면서 하나씩 result에 집어넣고
result = [K]
while K != N:
    result.append(arr[K])
    K = arr[K]
# 뒤집어서 출력
result.reverse()
print(*result)