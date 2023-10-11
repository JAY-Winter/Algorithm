'''
- 지훈이와 불은 매 분마다 4방향으로 이동한다
- 불은 각 지점에서 네 방향으로 확산된다
    다만, 벽이 있는 공간은 통과하지 못 한다
- 탈출 조건
    미로의 가장자리를 탈출할 때

Q) 지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
    지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
'''


# 지훈이의 초기 위치 찾기
def find_jihoon_init_position():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'J':
                return i, j


def find_fire_init_position():
    # 불의 초기 위치 찾기
    fire_position = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'F':
                fire_position.append((i, j))
    return fire_position


def main():
    init_r, init_c = find_jihoon_init_position()
    fire_position = find_fire_init_position()

    # 지훈이가 방문한 좌표 및 체크
    visited = [[False] * C for _ in range(R)]
    visited[init_r][init_c] = True

    # 지훈이의 위치 설정
    r, c, min = init_r, init_c, 0
    jihoon_position = [(r, c, min)]

    while True:
        # 불이 퍼진다
        new_fire_position = []
        for fire in fire_position:
            r, c = fire
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if R > nr >= 0 and C > nc >= 0 and board[nr][nc] == '.':
                    board[nr][nc] = 'F'
                    new_fire_position.append((nr, nc))

        # 불의 위치가 갱신된다
        fire_position = new_fire_position

        # 지훈이가 움직인다
        new_jihoon_position = []
        while jihoon_position:
            r, c, min = jihoon_position.pop(0)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                # 탈출 조건
                if nr >= R or nr < 0 or nc >= C or nc < 0:
                    return min + 1

                if board[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_jihoon_position.append((nr, nc, min + 1))

        # 지훈의 위치가 갱신되었는가? 즉, 움직일 수 있는가?
        if not new_jihoon_position:
            return 'IMPOSSIBLE'
        else:
            # 지훈의 위치가 갱신된다
            jihoon_position = new_jihoon_position


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# 사방향 탐색을 위한 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(main())
