N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def search_union(arr):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    union_list = []
    
    for i in range(N):
        visited = set()
        for j in range(N):
            union = set()
            visited.add((i, j))
            val = arr[i][j]
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]

                if nr >= N or nr < 0 or nc >= N or nc < 0:
                    continue
                
                if (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                new_val = arr[nr][nc]
                diff = abs(val - new_val)

                if L <= diff <= R:
                    union.add((i, j))
                    union.add((nr, nc))
            if union:
                union_list.append(union)
    # print(union_list)
    # print()
    return union_list

def moving(union, arr):
    sum_union = 0
    cnt_union = len(union)
    
    for country in union:
        r, c = country
        sum_union += arr[r][c]
    
    result_union = sum_union // cnt_union
    
    for country in union:
        r, c = country
        arr[r][c] = result_union

def moving2(union_list, arr):
    for union in union_list:

        sum_union = 0
        cnt_union = len(union)

        for country in union:
            r, c = country
            sum_union += arr[r][c]
    
        result_union = sum_union // cnt_union
        
        for country in union:
            r, c = country
            arr[r][c] = result_union

answer = 0
while True:
    union_list = search_union(arr)
    print(union_list)
    if union_list:
        moving2(union_list, arr)
        answer += 1
    else:
        break

print(answer)