from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(M)]

'''
(0, 0) -> (N-1, M-1) 로 이동하려면 벽을 최소 몇 개 부수어야 하는지?
'''

answer = 987654321

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    Q = deque([(0, 0, 0)])
    visited = [[-1] * N for _ in range(M)]
    visited[0][0] = True

    while Q:
        r, c, n = Q.popleft()

        if r == M - 1 and c == N - 1:
            return n

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < M and 0 <= nc < N:
                if arr[nr][nc] == 1 and (visited[nr][nc] == -1 or visited[nr][nc] > n + 1):
                    visited[nr][nc] = n + 1
                    Q.append((nr, nc, n + 1))
                elif arr[nr][nc] == 0 and visited[nr][nc] == -1:
                    visited[nr][nc] = n
                    Q.appendleft((nr, nc, n))

    return - 1


answer = bfs()
print(answer)
