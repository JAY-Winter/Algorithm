'''
- D 킬로미터 길이의 고속도로를 지난다
- 모든 지름길은 일방 통행이고, 고속도로를 역주행 할 수는 없다

Q) 운전해야 하는 거리의 최솟값

'''
# N : 지름길의 개수 , D : 고속도로의 길이
N, D = map(int, input().split())

INF = 987654321
distances_info = [INF] * (10001)
# print(distances)

distance_dict = {}

for _ in range(N):
    start, end, size = map(int, input().split())
    # 역주행 불가능
    if end > D:
        continue

    if start not in distance_dict:
        distance_dict[start] = [(end, size)]
    else:
        distance_dict[start] += [(end, size)]


def dijk():
    start_node = 0
    distances_info[start_node] = 0
    Q = [start_node]

    while Q:
        cur_node = Q.pop(0)

        if cur_node > D:
            continue
        # if cur_node == D:
        #     return distances_info[D]

        # 지름길이 존재할 때
        if distance_dict.get(cur_node):
            for end_node, shortcut in distance_dict[cur_node]:
                new_distance = distances_info[cur_node] + shortcut
                if new_distance < distances_info[end_node]:
                    distances_info[end_node] = new_distance
                    Q.append(end_node)

        # 직진도 확인
        new_node = cur_node + 1
        new_distance = distances_info[cur_node] + 1

        if new_distance < distances_info[new_node]:
            distances_info[new_node] = new_distance
            Q.append(new_node)


dijk()
print(distances_info[D])
