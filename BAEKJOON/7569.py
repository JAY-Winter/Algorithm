from pprint import pprint
from collections import deque

# M : 가로 칸 <= 100
# N : 세로 칸 <= 100
# H : 높이 <= 100
M, N, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N*H)]

# 1: 익은 토마토
# 0: 익지 않은 토마토
# -1 : 토마토가 없는 곳

# 토마토가 모두 익을 때 까지 최소 며칠이 걸리는지 계산
# 저장될 때 부터 모든 토마토가 익어있는 상태면 0 출력
# 토마토가 모두 익지 못하는 상황이면 - 1출력
tomatos_list = []
end_flag = False
for r in range(N*H):
    for c in range(M):
        if arr[r][c] == 1:
            tomatos_list.append((r, c))
        if arr[r][c] == 0:
            end_flag = True
# 하루가 지나면 인접한 곳(위, 아래, 왼쪽,오른쪽, 앞, 뒤) 토마토는 익게 됨

def bfs(tomatos_list):
    # visited = set()
    visited = [[0 for _ in range(M)] for _ in range(N*H)]
    Q = deque(tomatos_list)
    new_tomatos_list = deque()
    cnt = 0
    while Q:
        r, c = Q.popleft()
        
        visited[r][c] = 1
        for h in range(1, H+1):
            for x, y in ((+N*h, 0), (-N*h, 0), (0, 1), (0, -1), (1, 0), (-1, 0)):
                nr = r + x
                nc = c + y

                if nr >= N*H or nr < 0 or nc >= M or nc < 0:
                    continue

                if arr[nr][nc] == -1 or arr[nr][nc] == 1:
                    continue
                
                if visited[nr][nc]:
                    continue

                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1
                    visited[nr][nc] = 1
                    new_tomatos_list.append((nr, nc))
        if not Q:
            if new_tomatos_list:
                cnt += 1
            Q = deque(new_tomatos_list) 
            new_tomatos_list = deque()
    return cnt

if not end_flag:
    cnt = 0
else:
    cnt = bfs(tomatos_list)

for r in range(N*H):
    for c in range(M):
        if arr[r][c] == 0:
            cnt = -1
            break

print(cnt)

# Sol2

from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
queue = deque()

# 익은 토마토 위치 확인
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                queue.append((h, n, m, 0))

while queue:
    h, n, m, day = queue.popleft()
    for dh, dn, dm in directions:
        nh, nn, nm = h + dh, n + dn, m + dm
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and arr[nh][nn][nm] == 0:
            arr[nh][nn][nm] = 1
            queue.append((nh, nn, nm, day + 1))

# 토마토가 모두 익지 못하는 경우를 확인
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 0:
                print(-1)
                exit(0)

# 토마토가 모두 익는 데 걸리는 최소 일수 출력
print(day)
