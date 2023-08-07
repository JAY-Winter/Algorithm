from pprint import pprint

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def cal_zero(r, c, graph):
    cnt = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr >= N or nr < 0 or nc >= M or nc < 0:
            continue
        if graph[nr][nc] == 0:
            cnt += 1
    return cnt


def melting(infos):
    for info in infos:
        r, c, cnt = info
        graph[r][c] -= cnt
        if graph[r][c] < 0:
            graph[r][c] = 0


def bfs(r, c, visited):
    visited.add((r, c))
    Q = [(r, c)]
    infos = []
    while Q:
        r, c = Q.pop(0)
        zero_cnt = cal_zero(r, c, graph)
        infos.append((r, c, zero_cnt))

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if N > nr >= 0 and M > nc >= 0 and (nr, nc) not in visited and graph[nr][nc] > 0:
                Q.append((nr, nc))
                visited.add((nr, nc))
    melting(infos)


def main():
    cnt = 0
    while True:

        flag = False
        visited = set()
        group = 0
        for i in range(N):
            for j in range(M):
                if group >= 2:
                    return cnt
                if graph[i][j] and (i, j) not in visited:
                    flag = True
                    group += 1
                    bfs(i, j, visited)
        cnt += 1
        if not flag:
            return 0


answer = main()
print(answer)
