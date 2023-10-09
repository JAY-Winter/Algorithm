def search(n, prev, combinations):
    global answer_cost, answer_gredients

    if n > N:
        return

    # 최소 영양성분에 부합하는지 확인
    sum_p, sum_f, sum_s, sum_v = 0, 0, 0, 0
    for combination in combinations:
        gredient = gredients[combination]
        sum_p += gredient[0]
        sum_f += gredient[1]
        sum_s += gredient[2]
        sum_v += gredient[3]

    # 최소 비용 구하기
    if sum_p >= mp and sum_f >= mf and sum_s >= ms and sum_v >= mv:
        sum_cost = sum(costs[combination] for combination in combinations)

        # 값 비교
        if sum_cost <= answer_cost:
            # 작을 경우, answer_gredients 갱신
            if sum_cost < answer_cost:
                answer_cost = min(answer_cost, sum_cost)
                answer_gredients = [combinations]
            # 같을 경우, answer_gredienst 에 값 추가
            else:
                answer_gredients.append(combinations)

    # 조합 만들기
    for i in range(prev, N + 1):
        if not visited[i]:
            visited[i] = True
            search(n + 1, i, combinations + [i])
            visited[i] = False


N = int(input())
mp, mf, ms, mv = map(int, input().split())
# 케이스별(1번, 2번 .. N번) 재료를 나타내기 위한 2차원 배열
gredients = [[] for _ in range(N + 1)]
# 케이스별(1번, 2번 .. N번) 가격을 나타내기 위한 1차원 배열
costs = [0] * (N + 1)

for i in range(1, N + 1):
    p, f, s, v, c = map(int, input().split())
    gredients[i] = [p, f, s, v]
    costs[i] = c

# 조합 경우의 수를 만들기 위한 방문 배열
visited = [False] * (N + 1)
answer_cost = 987654321
answer_gredients = []
search(0, 1, [])
if answer_cost == 987654321:
    print(-1)
else:
    print(answer_cost)
    # 같은 비용의 집합이 하나 이상일 시,
    if len(answer_gredients) >= 2:
        print(*(sorted(answer_gredients)[0]))
    else:
        print(*(sorted(answer_gredients)[0]))
