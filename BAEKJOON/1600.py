'''
Q) 원숭이의 동작수의 최솟값을 출력하라
    도착할 수 없는 경우엔 -1 을 출력하라

'''
from collections import deque


def bfs():
    horse_dr = [-2, -2, -1, 1, 2, 2, 1, -1]
    horse_dc = [-1, 1, 2, 2, 1, -1, -2, -2]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[[False] * (K + 1) for _ in range(C)] for _ in range(R)]
    visited[0][0][K] = True

    if board[0][0] == 1:
        return - 1

    # r, c, 말처럼 이동할 수 있는 횟수, 동작 수
    Q = deque([(0, 0, K, 0)])
    while Q:
        r, c, k_cnt, dist = Q.popleft()

        if (r, c) == (R - 1, C - 1):
            return dist

        # 4방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if nr >= R or nr < 0 or nc >= C or nc < 0:
                continue

            if not visited[nr][nc][k_cnt] and board[nr][nc] == 0:
                visited[nr][nc][k_cnt] = True
                Q.append((nr, nc, k_cnt, dist + 1))

        # 8방 탐색
        if k_cnt > 0:
            for d in range(8):
                nr, nc = r + horse_dr[d], c + horse_dc[d]

                if nr >= R or nr < 0 or nc >= C or nc < 0:
                    continue

                if board[nr][nc] == 0 and not visited[nr][nc][k_cnt - 1]:
                    visited[nr][nc][k_cnt - 1] = True
                    Q.append((nr, nc, k_cnt - 1, dist + 1))
    return -1


K = int(input())
C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

print(bfs())
