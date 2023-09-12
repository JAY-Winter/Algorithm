N, K = map(int, input().split())

answer_cnt = 0


def bfs():
    global answer_cnt, K, N
    # 해당 위치에 도착하기까지 걸리는 시간
    time = [1e9] * 100001
    # 시작 위치 초기화
    time[N] = 0

    Q = [(N, 0)]
    while Q:
        # 현재 위치와 현재 위치까지 걸린 시간
        now, sec = Q.pop(0)

        # 현재 위치가 동생 위치 & 현재까지 걸린 시간이 K 까지 걸린 시간 보다 작거나 같을 경우
        if now == K and time[K] <= sec:
            answer_cnt += 1

        # 나아갈 위치
        for new_pos in (now + 1, now - 1, now * 2):
            # 범위 내 & 나아갈 위치까지의 걸린 시간이 현재 걸린 시간 + 1 보다 크거나 같을 경우 & 움직이더라도 K 까지 걸리는 시간보다 작아야함
            if 100000 >= new_pos >= 0 and time[new_pos] >= sec + 1 and time[K] >= sec + 1:
                Q.append((new_pos, sec + 1))
                time[new_pos] = sec + 1

    return time


time = bfs()

print(time[K])
print(answer_cnt)
