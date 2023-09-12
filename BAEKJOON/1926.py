N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def bfs(r, c, visited):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited[r][c] = True
    temp_cnt = 1
    Q = [(r, c)]
    while Q:
        r, c = Q.pop(0)

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue
            if visited[nr][nc]:
                continue
            if not graph[nr][nc]:
                continue

            visited[nr][nc] = True
            temp_cnt += 1
            Q.append((nr, nc))
    return temp_cnt


def search():
    visited = [[False] * M for _ in range(N)]
    answer_cnt = 0
    answer_size = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                temp_size = bfs(i, j, visited)
                answer_cnt += 1
                if temp_size > answer_size:
                    answer_size = temp_size
    return answer_cnt, answer_size


cnt, size = search()
print(cnt)
print(size)