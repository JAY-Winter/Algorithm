import sys
from collections import deque


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 행, 열, 부순 벽의 수
    Q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while Q:
        r, c, broken_walls = Q.popleft()

        if r == N - 1 and c == M - 1:
            return visited[r][c][broken_walls]

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if N > nr >= 0 and M > nc >= 0:
                # 벽을 만난 경우
                if board[nr][nc] == 1 and broken_walls < K and not visited[nr][nc][broken_walls + 1]:
                    visited[nr][nc][broken_walls + 1] = visited[r][c][broken_walls] + 1
                    Q.append((nr, nc, broken_walls + 1))
                # 빈 칸을 만난 경우
                elif board[nr][nc] == 0 and not visited[nr][nc][broken_walls]:
                    visited[nr][nc][broken_walls] = visited[r][c][broken_walls] + 1
                    Q.append((nr, nc, broken_walls))

    return -1


input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

print(bfs())

from pprint import pprint
pprint(visited)
