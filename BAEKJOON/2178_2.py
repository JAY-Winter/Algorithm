from collections import deque

N, M = map(int, input().split())
arrs = [list(map(int,input().strip())) for _ in range(N)]

# 1: 이동가능
# 0: 이동불가능

# (0, 0) 에서 시작해서 (N-1, M-1) 도착할 때 이동하는 최소 칸수
# 인접만 가능

answer = 987654321
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0 for _ in range(M)] for _ in range(N)]
print(visited)
def bfs(start_r, start_c):
    global answer
    Q = deque([(start_r, start_c, 1)])
    while Q:
        r, c, cnt = Q.popleft()
        visited[r][c] = 1
        if r == N-1 and c == M-1:
            if answer > cnt:
                answer = cnt
            return
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if N > nr >= 0 and M > nc >= 0 and arrs[nr][nc] == 1 and not visited[nr][nc]:
                Q.append((nr, nc, cnt + 1))

start_r = 0
start_c = 0

bfs(start_r, start_c)
print(answer)
