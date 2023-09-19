from collections import deque

N, M, gas = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi_r, taxi_c = map(lambda x: x - 1, map(int, input().split()))

passengers = [list(map(lambda x: x - 1, map(int, input().split()))) for _ in range(M)]

'''
1. 현재 택시의 위치에서 모든 승객들에 대한 거리를 구한다
2. 가장 가까운 승객에게 도달하는 거리 + 목적지까지 거리 <= 남은 가스의 양
    인지 판단한다
    실패시 -1 리턴 하면서 끝
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def cal_distance(where, to):
    from_r, from_c = where
    to_r, to_c = to
    distance = 0

    if from_r == to_r and from_c == to_c:
        return distance

    visited = set((from_r, from_c))
    Q = deque([(from_r, from_c, distance)])

    while Q:
        r, c, distance = Q.popleft()
        if r == to_r and c == to_c:
            return distance
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if N > nr >= 0 and N > nc >= 0 and (nr, nc) not in visited and arr[nr][nc] == 0 and distance < gas:
                visited.add((nr, nc))
                Q.append((nr, nc, distance + 1))
    return -1


# 문제가 택시 위치에서 승객까지의 모든 거리를 순차적으로 구하려고 하다보니 시간 초과가 발생함
# 따라서, 택시 위치에서 BFS 탐색하면서 모든 승객의 위치를 리스트에 담은 후, 승객 선별
def take_passenger():
    global passengers, taxi_r, taxi_c

    visited = set((taxi_r, taxi_c))
    Q = deque([(taxi_r, taxi_c, 0)])
    potential_passengers = []
    while Q:
        r, c, distance = Q.popleft()
        if len(potential_passengers) == len(passengers):
            took_passenger = sorted(potential_passengers, key=lambda x: (x[0], x[1], x[2]))[0]
            return took_passenger
        # 현재 택시 위치와 승객이 서있는 위치와 같을 시
        for idx, passenger in enumerate(passengers):
            if (r, c) == (passenger[0], passenger[1]):
                potential_passengers.append((distance, *passenger, idx))
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if N > nr >= 0 and N > nc >= 0 and (nr, nc) not in visited and arr[nr][nc] == 0 and distance < gas:
                visited.add((nr, nc))
                Q.append((nr, nc, distance + 1))

    # 택시가 모든 승객의 위치에 도달하지 못 할경우
    if not potential_passengers:
        return -1

    # 승객 선별
    took_passenger = sorted(potential_passengers, key=lambda x: (x[0], x[1], x[2]))[0]
    return took_passenger


def search():
    global gas, passengers, taxi_r, taxi_c

    while passengers:
        # 선별된 승객
        passenger = take_passenger()

        if passenger == -1:
            return -1

        passengers.pop(passenger[-1])

        distance_from_taxi_to_passenger = passenger[0]
        gas -= distance_from_taxi_to_passenger

        if gas < 0:
            return -1

        distance_from_passenger_to_destination = cal_distance((passenger[1], passenger[2]),
                                                              (passenger[3], passenger[4]))
        if distance_from_passenger_to_destination == -1:
            return -1

        gas -= distance_from_passenger_to_destination

        if gas < 0:
            return -1

        gas += 2 * distance_from_passenger_to_destination
        taxi_r, taxi_c = passenger[3], passenger[4]

    return gas


answer = search()
print(answer)
