
# 0 : 빈 칸
# 1 : 집
# 2 : 치킨집
# 집의 개수는 2N 개를 넘지 않으며, 적어도 1개는 존재한다
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다

# r, c 는 1부터 시작한다 -> 1씩 뺴야함

# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
# 즉, 집을 기준으로 거리가 정해지며, 각각의 집은 치킨 거리를 가지고 있다

# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다
# 임의의 두 칸 거리 : |r1-r2| + |c1-c2|

# 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개
# Q : 최대 M 개를 고르고, 도시의 치킨거리가 가장 작게될지를 구하라


# 1. 모든 치킨집의 좌표를 구한다
# 2. 모든 집의 좌표를 구한다
# 3. 치킨 집중 M 개만 골라서 모든 집과의 치킨거리를 구한다
# 4. 치킨 거리를 구하면서 가장 작은 값을 answer 로 둔다


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houst_list = []
chicken_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken_list.append((i, j)) 
        elif arr[i][j] == 1:
            houst_list.append((i, j))

chicken_list_cnt = len(chicken_list)
visited = [0 for _ in range(chicken_list_cnt)]

answer = 987654321

def cal_distance(houses, chicken_list, cases):
    global answer
    chicken_distance = 0

    for house in houses:
        h_r, h_c = house
        temp_distance = 987654321
        for case in cases:
            c_r, c_c = chicken_list[case]
            distance = abs(h_r - c_r) + abs(h_c - c_c)
            if distance < temp_distance:
                temp_distance = distance
        chicken_distance += temp_distance
    
    if answer > chicken_distance:
        answer = chicken_distance
    

def set_permutation(n, cases, start):
    if n == M:
        cal_distance(houst_list, chicken_list, cases)
        return
    
    for i in range(start, chicken_list_cnt):
        if not visited[i]:
            visited[i] = 1
            set_permutation(n+1, cases+[i], i)
            visited[i] = 0


set_permutation(0, [], 0)

print(answer)