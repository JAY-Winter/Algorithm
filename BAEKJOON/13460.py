from collections import deque

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]
check = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
Q = deque()


def init():
    _rx, _ry, _bx, _by = [0] * 4
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                _rx, _ry = i, j
            elif board[i][j] == 'B':
                _bx, _by = i, j
    Q.append((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True


def move(_x, _y, _dx, _dy, cnt):
    while board[_x + _dx][_y + _dy] != '#' and board[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        cnt += 1
    return _x, _y, cnt


def bfs():
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

    while Q:
        rx, ry, bx, by, cnt = Q.popleft()
        if cnt >= 10:
            break
        for d in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[d], dy[d], 0)
            nbx, nby, bcnt = move(bx, by, dx[d], dy[d], 0)
            # blue 가 빠진 경우
            if board[nbx][nby] == 'O':
                continue
            # 정답 비교
            if board[nrx][nry] == 'O':
                print(cnt+1)
                return
            if nrx == nbx and nry == nby:
                # R 이 뒤에 있었음
                if rcnt > bcnt:
                    nrx, nry = nrx - dx[d], nry - dy[d]
                # B 가 뒤에 있었음
                else:
                    nbx, nby = nbx - dx[d], nby - dy[d]
            # 해당 경우로 방문하지 않은 경우
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                Q.append((nrx, nry, nbx, nby, cnt + 1))
    print(-1)


init()
bfs()
