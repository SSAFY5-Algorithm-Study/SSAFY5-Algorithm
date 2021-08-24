N = int(input())
num_list = []
for i in range(N):
    if i == 0:
        num_list.append(int(input()))
        continue
    current_number = int(input())
    if current_number == 0:
        num_list.pop()
    else:
        num_list.append(current_number)
print(sum(num_list))
        
