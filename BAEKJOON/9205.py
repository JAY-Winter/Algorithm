t = int(input())


def cal_distance(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])


def move(now):
    can_move = 1000
    Q = [now]

    while Q:
        cur = Q.pop(0)
        if cal_distance(cur, festival) <= can_move:
            return 'happy'

        for idx, store in enumerate(sorted_store):
            distance = cal_distance(cur, store)
            if distance <= can_move and not visited[idx]:
                visited[idx] = True
                Q.append(store)

    return 'sad'


for _ in range(t):
    n = int(input())
    home = []
    store = []
    festival = []
    visited = [False for _ in range(n)]
    for i in range(n + 2):
        if i == 0:
            home = list(map(int, input().split()))
        elif i == n + 1:
            festival = list(map(int, input().split()))
        else:
            store.append(list(map(int, input().split())))

    sorted_store = sorted(store, key=lambda x: cal_distance(home, x))

    print(move(home))
