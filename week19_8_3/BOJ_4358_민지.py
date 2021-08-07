tree_dict = {}
total = 0

while True:
    tree = input()
    if tree == "":
        break
    tree_dict[tree] = tree_dict.get(tree, 0) + 1
    total += 1

for k, v in sorted(tree_dict.items()):
    print(k, round(v/total * 100, 4))