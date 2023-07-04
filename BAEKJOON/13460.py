# 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 뺴내는 게임
# 세로 : N, 가로 : M
# 가장 바깥 행과 열은 모두 막혀져있고, 보드에는 구멍이 하나 있다
# 파란 구슬이 구멍에 들어가면 안 된다

# 각각의 동작에서 공은 동시에 움직인다
# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패다
# 빨가 ㄴ구슬과 파란 구슬이 동시에 구멍에 빠져도 실패
# 동시에 같은 칸에 있을 수 없다
# 

# 기울이는 동작을 그만 하는 기준 : 더 이상 구슬이 움직이지 않을 때 까지

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
print(arr)

# . : 빈 칸
# # : 이동할 수 없음
# 0 : 구멍의 위치
# R : 빨간 구슬의 위치
# B : 파란 구슬의 위치

# Q : 최소 몇 번 만에 빨간 구슬을 구멍을 통해 뺴낼 수 있는지 출력
# 만약 10 번 이하로 움직여서 빨간 구슬을 구멍을 통해 뺴낼 수 없으면 -1 출력

def left(balls):
    pass

def right(balls):
    pass

def up(balls):
    pass

def down(balls):
    pass

def find_balls():
    balls = set()
    for r in range(N):
        for c in range(M): 
            if arr[r][c] == 'R' or arr[r][c] == 'B':
                balls.add((r, c))
    return balls

i = 0
while i < 10:
    balls = find_balls()

    for ball_pos in balls:
        r, c = ball_pos
        left()


    i += 1
    pass
