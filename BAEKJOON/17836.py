'''
Q. 용사가 제한 시간 T 이내에 공주에게 도달할 수 있다면, 공주에게 도달할 수 있는 최단시간을 출력하라
    만약, 구출할 수 없다면 "Fail" 을 출력한다

- 시작은 (0, 0)
- 그람을 구하게 되면 무제한으로 사용할 수 있다
- 0 : 빈 공간
- 1 : 벽
- 2 : 그람이 있는 공간
- N, M <= 100
'''

from collections import deque


def bfs():
    global answer

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 0

    Q = deque([(0, 0, False)])
    while Q:
        r, c, get_gram = Q.popleft()

        if r == N - 1 and c == M - 1:
            answer = min(answer, visited[r][c][get_gram])

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue

            if arr[nr][nc] == 2 and not get_gram:
                visited[nr][nc][1] = visited[r][c][get_gram] + 1
                Q.append((nr, nc, True))

            if visited[nr][nc][get_gram]:
                continue

            if arr[nr][nc] == 0 or (get_gram and arr[nr][nc] == 1):
                visited[nr][nc][get_gram] = visited[r][c][get_gram] + 1
                Q.append((nr, nc, get_gram))


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 10001
bfs()
print(answer) if answer <= T else print("Fail")
