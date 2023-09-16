'''
Q: 100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는가?

- 주사위는 1 ~ 6 까지 던질 수 있다
- 각 칸마다 해당 칸에 몇 번의 횟수를 통해 도착할 수 있는가? 가 관건
- 다만, 특정 칸에 이동할 수 있는 특이점이 있음
- 따라서, 1번 칸에 시작해서 이동할 때 마다 1 ~ 6번까지의 모든 경우에 대해 탐색
- 탐색하는 과정 중 아래와 같은 조건을 확인해야함
- 1) 게임판을 벗어나거나 (1  ~ 100)
- 2) 이동하려는 칸에 도착하기 까지의 횟수가 현재 진행된 횟수보다 적거나
- 3) 이동하려는 칸이 사다리 정보 혹은 뱀 정보가 있는가
'''

N, M = map(int, input().split())

# 사다리 정보
ladders = [0 for _ in range(101)]
for _ in range(N):
    # x번 칸에 도착하면, y번칸으로 이동한다
    x, y = map(int, input().split())
    ladders[x] = y

# 뱀 정보
snakes = [0 for _ in range(101)]
for _ in range(M):
    # u번 칸에 도착하면, v번 칸으로 이동한다
    u, v = map(int, input().split())
    snakes[u] = v


def search():
    # 각 칸마다 도착 횟수
    rolls = [1e9 for _ in range(101)]
    rolls[1] = 0

    # 초기값 선언
    start_num = 1
    roll_cnt = 0

    # BFS
    Q = [(start_num, roll_cnt)]
    while Q:
        cur_pos, cur_cnt = Q.pop(0)

        if cur_pos == 100:
            return cur_cnt

        for d in range(1, 7):
            # 업데이트 정보
            new_pos = cur_pos + d
            new_cnt = cur_cnt + 1

            # 게임판 범위 확인
            if new_pos > 100 or new_pos < 1:
                continue

            # 이동 횟수 확인
            if rolls[new_pos] <= new_cnt:
                continue

            # 사다리, 뱀 정보 확인 및 Q, rolls 업데이트
            if ladders[new_pos]:
                Q.append((ladders[new_pos], new_cnt))
                rolls[ladders[new_pos]] = new_cnt
            elif snakes[new_pos]:
                Q.append((snakes[new_pos], new_cnt))
                rolls[snakes[new_pos]] = new_cnt
            else:
                Q.append((new_pos, new_cnt))
                rolls[new_pos] = new_cnt

    return rolls[100]


answer = search()
print(answer)
