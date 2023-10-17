'''
시작 : (0,0)
도착 : (N-1, N-1)

잃은 금액을 최소로 하여 도착해야한다
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = 1

while True:

    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]

    distance = [[987654321 for _ in range(N)] for _ in range(N)]
    distance[0][0] = board[0][0]

    Q = [(0, 0)]
    while Q:
        r, c = Q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue

            if distance[nr][nc] > distance[r][c] + board[nr][nc]:
                distance[nr][nc] = distance[r][c] + board[nr][nc]
                Q.append((nr, nc))

    print(f'Problem {T}:', distance[N - 1][N - 1])

    T += 1
