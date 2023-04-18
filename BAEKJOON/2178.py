N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

dr = [-1 , 1, 0, 0]
dc = [0, 0, -1, 1]
Q = [(0, 0)]
answer = 0

while Q:
    r, c = Q.pop(0)
    if r == N - 1 and c == M - 1:
        answer = arr[N-1][M-1]
        break
    
    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]
        
        if new_r >= N or new_r < 0 or new_c >= M or new_c < 0:
            continue
            
        if arr[new_r][new_c] == 0:
            continue
            
        if arr[new_r][new_c] == 1:    
            arr[new_r][new_c] = arr[r][c] + 1
            Q.append((new_r, new_c))

    
    
print(answer)