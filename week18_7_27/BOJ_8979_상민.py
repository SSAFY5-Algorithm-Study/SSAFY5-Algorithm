def get_ans():
    if len(scores_sorted) == 1:
        return 1
    for idx, score in enumerate(scores_sorted):
        nation, g, s, b = score
        num = int(''.join(map(str, [g, s, b])))
        if idx == 0:
            if nation == K:
                return rank[0]
            standard = num
            continue
        if num == standard:
            if nation == K:
                return rank[0]
            same_rank[0] += 1
            continue
        else:
            rank[0] += 1
            if same_rank[0]:
                rank[0] += same_rank[0]
                same_rank[0] = 0
            if nation == K:
                return rank[0]
            standard = num


N, K = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]
scores_sorted = sorted(scores, key= lambda x: (-x[1], -x[2], -x[3]))

rank = [1]
same_rank = [0]
print(get_ans())
            