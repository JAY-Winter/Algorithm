from collections import deque

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    visited = [[0] * C for _ in range(R)]
    Q = deque([(r, c, 1)])
    while Q:
        r, c, cnt = Q.popleft()
        visited[r][c] = cnt
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if R > nr >= 0 and C > nc >= 0 and not visited[nr][nc] and graph[nr][nc] == 'L':
                Q.append((nr, nc, cnt+1))
    print('r', 'c', r, c)
    return visited[r][c] - 1


def solution():
    answer = -1e9
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 'L':
                print(r, c)
                cnt = bfs(r, c)
                answer = max(answer, cnt)
                print()
    return answer


answer = solution()
print(answer)
