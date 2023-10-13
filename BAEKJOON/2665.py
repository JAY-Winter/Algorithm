'''
- N * N 의 보드
    0 : 검은 방 -> 못 들어감
    1 : 흰 방

- 시작점 : (0, 0)
- 끝 점 : (N-1, N-1)

- 시작방에서 출발해, 끝방으로 가는 것이 목적이다
    이때, 검은 방 몇 개를 흰 방으로 바꾸어서 도착하고 싶다

Q) 방 색을 바꾸어야 할 최소의 수를 구하라
    단, 하나도 바꾸지 않고 도착할 경우 0 을 출력
'''


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 해당 좌표까지 도달하기에, 몇 번 방 색을 바꾸면서 왔는지
    visited = [[1e9] * N for _ in range(N)]
    visited[0][0] = 0

    # (0, 0) 시작, 0개 바꿈
    Q = [(0, 0, 0)]
    while Q:
        r, c, change = Q.pop(0)

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위를 벗어난 경우
            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue

            # 검은 방일 경우
            if board[nr][nc] == 0 and visited[nr][nc] > change + 1:
                visited[nr][nc] = change + 1
                Q.append((nr, nc, change + 1))

            # 흰색 방일 경우
            if board[nr][nc] == 1 and visited[nr][nc] > change:
                visited[nr][nc] = change
                Q.append((nr, nc, change))

    return visited[N - 1][N - 1]


N = int(input())
board = [list(map(int, input())) for _ in range(N)]

answer = bfs()
print(answer)
