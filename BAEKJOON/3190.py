'''
- 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다
- 보드의 상하좌우 끝에 벽이 있다
- 게임이 시작할 때, 뱀은 (1,1) 에 위치하고 길이는 1이고 오른쪽을 향한다
- 몇 몇 칸에는 사과가 놓여져있다

- 뱀의 이동 규칙
    - 매 초마다 이동한다
    1. 몸 길이를 늘려 머리를 다음 칸에 위치시킨다
    1-1. 벽이나 자기자신의 몸과 부딪히면 끝
    2. 이동한 칸에 사과가 있다면, 사과는 없어지고 꼬리는 움직이지 않는다
    2-1. 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
        즉, 몸길이는 변하지 않는다

Q. 사과의 위치와 뱀의 이동경로가 주어질 때, 게임이 몇 초에 끝나는지 계산하라
'''


def play():
    sec = 0
    # 뱀의 초기 위치, 머리 방향
    init_r, init_c, init_d = (0, 0, 1)

    # 뱀의 몸의 위치 리스트
    snake_position = [(init_r, init_c)]

    # 뱀의 방향 변환 정보 :  상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while True:
        # 뱀은 매 초마다 이동을 한다
        sec += 1

        # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다
        head_r, head_c = snake_position[0]
        new_head_r, new_head_c = head_r + dr[init_d], head_c + dc[init_d]

        # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다
        if new_head_r >= N or new_head_r < 0 or new_head_c >= N or new_head_c < 0 or \
                (new_head_r, new_head_c) in snake_position:
            # 게임이 끝난다
            return sec

        # 머리를 다음 칸에 위치시킨다
        snake_position.insert(0, (new_head_r, new_head_c))

        # 만약 이동한 칸에 사과가 있다면
        if board[new_head_r][new_head_c] == 1:
            # 칸에 있던 사과는 없어지고 꼬리는 움직이지 않는다
            board[new_head_r][new_head_c] = 0
        # 만약 이동한 칸에 사과가 없다면
        else:
            # 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다
            snake_position.pop()

        # 게임 시작 시간으로부터 X초가 끝난 뒤에 방향 전환이 일어난다
        if sec in snake_direction:
            if snake_direction[sec] == 'D':
                init_d = (init_d + 1) % 4
            elif snake_direction[sec] == 'L':
                init_d = (init_d - 1) % 4


# 보드의 크기
N = int(input())
# 사과의 개수

K = int(input())

# 사과의 위치
apple_position = []
for _ in range(K):
    r, c = map(int, input().split())
    apple_position.append((r, c))

# 뱀의 방향 변환 횟수
L = int(input())
# 뱀의 방향 변환 정보
snake_direction = {}

for _ in range(L):
    X, C = input().split()
    # 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽 또는 오른쪽으로 90도 방향을 회전하라
    # L : 왼쪽, D : 오른쪽
    snake_direction[int(X)] = C

# board 초기화
board = [[0] * N for _ in range(N)]

# 사과 정보 초기화
for apple in apple_position:
    r, c = apple
    board[r - 1][c - 1] = 1

# 출력
print(play())
