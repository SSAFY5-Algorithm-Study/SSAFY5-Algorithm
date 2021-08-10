import sys
input = sys.stdin.readline

tree_dict = {}
total = 0

while True:
    tree = input().rstrip()
    if not tree:
        break

    tree_dict[tree] = tree_dict.get(tree, 0) + 1
    total += 1

for k, v in sorted(tree_dict.items()):
    # %.4f로 안해서 틀렸다...ㅂㄷㅂㄷ
    print(k, '%.4f' % round(v/total * 100, 4))