'''
- 0 : 빈 칸
- 1 : 아기 상어가 있는 칸

Q. 안전거리가 가장 큰 칸을 구해라
- 안전거리
    - 그 칸과 가장 거리가 가까운 아기 상어와의 거리
    - 두 칸의 거리 : 다른 칸으로 가기 위해 지나야하는 칸의 수
    - 이동은 인접한 8방향으로 가능
'''
from collections import deque


def calculate_distance(r, c):
    distance = [[-1] * M for _ in range(N)]
    distance[r][c] = 0
    Q = deque([(r, c)])
    while Q:
        r, c = Q.popleft()

        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]

            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue

            if board[nr][nc] == 1:
                return distance[r][c] + 1

            if distance[nr][nc] == -1:
                distance[nr][nc] = distance[r][c] + 1
                Q.append((nr, nc))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = -1

# 8방향 탐색
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 탐색
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            distance = calculate_distance(i, j)
            answer = max(answer, distance)

print(answer)
