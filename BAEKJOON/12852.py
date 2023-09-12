from collections import deque

X = int(input())

answer_route = ''
answer_cnt = 1e9


def bfs(X):
    global answer_route, answer_cnt
    Q = deque([(X, 0, '')])
    while Q:
        cur, cnt, route = Q.popleft()
        if cur == 1:
            if cnt < answer_cnt:
                answer_route = route + ' 1'
                answer_cnt = cnt
                return
        if cur % 3 == 0:
            Q.append((cur // 3, cnt + 1, route + ' ' + str(cur)))
        if cur % 2 == 0:
            Q.append((cur // 2, cnt + 1, route + ' ' + str(cur)))
        Q.append((cur - 1, cnt + 1, route + ' ' + str(cur)))


bfs(X)
print(answer_cnt)
print(answer_route[1:])
