N, K = map(int, input().split())
people = list(range(N))

answer = []
idx = 0
people_length = len(people)
while people:
  idx = (idx + K - 1) % people_length
  answer.append(people.pop(idx) + 1)
  people_length -= 1
print('<' + ', '.join(map(str, answer)) + '>')


