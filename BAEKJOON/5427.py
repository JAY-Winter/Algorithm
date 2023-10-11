'''
- 매 초마다 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져 나간다
- 벽에는 불이 붙지 않는다
- 상근이는 매초 인접한 칸으로 이동할 수 있다
    벽을 통과할 수 없다
    불이 옮겨진 칸 또는 옮겨질 칸으로 이동할 수 없다
    상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다

- 불이 붙는다
    빈 공간
    상근이가 있는 곳

Q) 얼마나 빨리 빌딩을 탈출할 수 있는지

0. 상근이의 위치를 찾는다
1. 불이 위치한 포지션을 찾는다
2. 불이 위치한 포지션으로부터 불이 퍼질 새로운 포지션을 잡는다
3. 상근이가 이동한다
    이때, 불이 퍼져있는 곳, 퍼질 곳, 벽은 안된다
'''


def main():
    # 상근이의 초기 위치를 찾는다
    init_r, init_c = 0, 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                init_r, init_c = i, j
                break

    # 불의 초기 위치를 찾는다
    fire_position = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire_position.append((i, j))

    # 상근이의 위치와 해당 위치까지 도달한 시간을 포함하고 있는 리스트
    sang_position = [(init_r, init_c, 0)]
    visited = [[False] * w for _ in range(h)]
    visited[init_r][init_c] = True

    while True:
        new_fire_position = []

        # 불이 퍼진다
        for fire in fire_position:
            fr, fc = fire
            for d in range(4):
                nfr, nfc = fr + dr[d], fc + dc[d]
                if h > nfr >= 0 and w > nfc >= 0 and board[nfr][nfc] == '.':
                    board[nfr][nfc] = '*'
                    new_fire_position.append((nfr, nfc))

        # 불의 위치가 갱신된다
        fire_position = new_fire_position

        # 상근이가 움직인다
        new_sang_position = []
        for sang in sang_position:
            r, c, sec = sang
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                # 탈출 완료
                if nr >= h or nr < 0 or nc >= w or nc < 0:
                    return sec + 1

                if board[nr][nc] == '.' and not visited[nr][nc]:
                    new_sang_position.append((nr, nc, sec + 1))
                    visited[nr][nc] = True

        # 더이상 움직일 곳이 없을 때
        if not new_sang_position:
            return 'IMPOSSIBLE'
        else:
            sang_position = new_sang_position


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    print(main())
