N = int(input())
T = int(input())
votes = list(map(int, input().split()))
spaces = []
nums_existed = set()
for vote in votes:
    if N == 1:
        if spaces:
            target, current_vote = spaces[0]
            if target == vote:
                spaces[0][1] += 1
            else:
                if current_vote > 1:
                    break
                else:
                    spaces[0] = [vote, 1]
        else:
            spaces.append([vote, 1])
    elif vote in nums_existed or len(spaces) < N:
        if spaces:
            for i in range(len(spaces)):
                target, current_vote = spaces[i]
                if target == vote:
                    spaces[i][1] = current_vote + 1
                    break
            else:
                spaces.append([vote, 1])
                nums_existed.add(vote)
        else:
            spaces.append([vote, 1])
            nums_existed.add(vote)
    else:
        min_vote, min_idx = 987654321, 0
        for i in range(N-1, -1, -1):
            target, current_vote = spaces[i]
            if current_vote <= min_vote:
                min_vote = current_vote
                min_idx = i
        nums_existed.remove(spaces[min_idx][0])
        spaces.pop(min_idx)
        spaces.append([vote, 1])
        nums_existed.add(vote)
print(' '.join(sorted([str(key) for key, value in spaces])))