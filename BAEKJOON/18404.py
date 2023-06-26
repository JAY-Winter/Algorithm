from collections import deque

def search(r, c, distance):
    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]

    cnt = 0
    Q = deque([(r, c)]) 
    distance[r][c] = 0
    while Q:
        r, c = Q.popleft()

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue
            
            if distance[nr][nc] != -1:
                continue

            distance[nr][nc] = distance[r][c] + 1
            Q.append((nr, nc))
        
# N <= 500, M <= 1000
# N*N 크기
# M 개의 상대편 말
N, M = map(int, input().split())
#현재 나이트의 위치 (X-1, Y-1)
X, Y = map(int, input().split())
distance = [[-1 for _ in range(N)] for _ in range(N)]

result = search(X-1, Y-1, distance)
for _ in range(M):
    # 상대편 말의 위치 (A-1, B-1)
    A, B = map(int, input().split())    
    # 순서대로 최소 이동 수를 구해야함
    print(distance[A-1][B-1], end=' ')
