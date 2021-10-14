#  def solution(sizes):
#     cards = []
#     for a, b in sizes:
#         if a > b:
#             cards.append([a, b])
#         else:
#             cards.append([b, a])
    
#     max_a = max([c[0] for c in cards])
#     max_b = max([c[1] for c in cards])
    
#     return max_a * max_b

# 배열에 저장 안하고 풀어보자!
# 최소 중에 최대 X 최대 중에 최대만 만들면 됨
def solution(sizes):
    min_len = max_len = 0
    for size in sizes:
        a, b = sorted(size)
        min_len = max(a, min_len)
        max_len = max(b, max_len)
    
    return min_len * max_len