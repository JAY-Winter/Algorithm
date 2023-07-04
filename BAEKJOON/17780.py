'''
N*N 체스판
K : 사용하는 말의 개수
하나의 말 위에 다른 말을 올릴 수 있다
체스판은 흰색, 빨간색, 파란색 중 하나로 칠해짐

게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1번~K번까지 번호가 매겨져있음
이동 방향도 미리 정해져 있음(상하좌우 중 하나)


1턴 : 1번 말 ~ K번 말까지 순서대로 이동
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동하며, 가장 아래에 있는 말만 이동할 수 있다
말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다.
턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다

A번 말이 이동 가능 경우
1. 이동하려고하는 칸이 흰색인 경우
- 이미 칸에 말이 있는 경우 가장 위에 A번 말을 올린다
2. 빨간색인 경우
- 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다
3. 파란색
- A번 말의 이동방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 한 후에 이동하려는 칸이
파란색인 경우에는 이동하지 않고 방향만 반대로 바꾼다
4. 체스판을 벗어나는 경우는 파란색과 동일

Q : 게임이 종료되는 턴의 번호를 구하라
그 값이 1000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1 을 출력한다

'''

# N : 체스판의 크기
# K : 말의 개수
N, K = map(int, input().split())

chess = [list(map(int, input().split())) for _ in range(N)]
horses = [[[] for _ in range(N)] for _ in range(N)]
horse_info = [[] for _ in range(K+1)]
for i in range(1, K+1):
    r, c, move = map(int, input().split())
    horse_info[i] = [r, c, move]

def is_four(nr, nc):
    if len(horses[nr][nc]) >= 4:
        return True
    else:
        return False

def white(now_pos, move_pos):
    r, c = now_pos
    nr, nc = move_pos

    A_horse = horses[r][c]
    horses[nr][nc] += A_horse
    return is_four(nr, nc)

def red(now_pos, move_pos):
    r, c = now_pos
    nr, nc = move_pos

    A_horse = horses[r][c]
    if len(A_horse) >= 2:
        A_horse = horses[r][c][::-1]
    horses[nr][nc] += A_horse
    return is_four(nr, nc)

def blue(now_pos, move_pos, move, horse_num):
    r, c = now_pos
    nr, nc = move_pos

    if move == 0:
        move = 1
    elif move == 1:
        move = 0
    elif move == 2:
        move = 3
    elif move == 3:
        move = 2

    nr += dr[move]
    nc += dc[move]
    if horses[nr][nc] == 2:
        horse_info[horse_num][2] = move
    else:
        horses[nr][nc] += horses[r][c]
    
    return is_four(nr, nc)

# 오른쪽, 왼쪽, 위, 아래
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

while True:
    for horse_num in range(1, len(horse_info)):
        horse = horse_info[horse_num]
        r, c, move = horse
        r -= 1
        c -= 1
        move -= 1
        horses[r][c].append(horse_num)
        nr = r + dr[move]
        nc = c + dc[move]
        now_pos = (r, c)
        move_pos = (nr, nc)
        flag = False
        if nr >= N or nr < 0 or nc >= N or nc < 0:
            if blue(now_pos, move_pos, move, horse_num):
                flag = True
                break
        else:
            color = chess[nr][nc]
            if color == 0:
                if white(now_pos, move_pos):
                    flag = True
                    break
            elif color == 1:
                if red(now_pos, move_pos):
                    flag = True
                    break
            elif color == 2:
                if blue(now_pos, move_pos, move, horse_num):
                    flag = True
                    break
        horses[r][c] = []

        if flag:
            break
