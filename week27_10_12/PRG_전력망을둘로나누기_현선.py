def solution(n, wires):
    answer = -1
    
    def BFS(n):
        q = [n]
        visited[n] = 1
        cnt = 0
        while q:
            x = q.pop(-1)
            for i in AL[x]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1
        # print(cnt)
        return cnt
        
            
        
    answer_list = []
    for p in range(n-1):
        AL = [[] for _ in range(n+1)]
        for i in range(n-1):
            if p == i:
                continue
            AL[wires[i][0]].append(wires[i][1])
            AL[wires[i][1]].append(wires[i][0])
        # print(AL)
        visited = [0 for _ in range(n+1)]
        result = 0
        for i in range(1,n+1):
            for j in range(len(AL[i])):
                # if visited[AL[i][j]]:
                #     continue
                result = BFS(AL[i][j])
                break
        #     result = n-2-result
            if result > 0:
                break
        # print(result)
        
        if result != n-2:
            answer_list.append(result)
    # print(answer_list)
    if len(answer_list) == 1:
        answer = answer_list[0]-answer_list[0]
    else:
        min_cnt = 101
        for i in range(len(answer_list)-1):
            for j in range(i+1, len(answer_list)):
                k = answer_list[i] - answer_list[j]
                # print(i,j)
                if abs(k) < min_cnt:
                    min_cnt = abs(k)
        answer = min_cnt
    # print(answer_list)
    # print(answer)
    return answer