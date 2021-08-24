# 5 4
# 3 1
# 3 2
# 4 3
# 5 3
from collections import deque
import sys
input = sys.stdin.readline

N, M =  map(int, input().split())
computer_relations = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    computer_relations[s].append(e)

for computer_relation in computer_relations:
    visited = [0] * (N + 1)
    if not computer_relation:
        continue
    else:
        queue = deque(computer_relation)
        while queue:
            target_computer = queue.popleft()
            visited[target_computer] = 1
            # print(target_computer, answer, computer_relations)
            answer[target_computer] += 1
            for adj in computer_relations[target_computer]:
                if not visited[adj]:
                    queue.append(adj)
result = [i for i in range(len(answer)) if answer[i] == max(answer)]
print(' '.join(map(str, result)))
