N = int(input())
infos = [[] for _ in range(N)]
for i in range(N):
    T, P = map(int, input().split())
    infos[i] = [T, P]


answer = 0


def dfs(day, sum_price):
    global answer

    if day >= N:
        answer = max(answer, sum_price)
        return

    # 현재 날짜의 상담을 진행하는 경우
    if day + infos[day][0] <= N:
        dfs(day + infos[day][0], sum_price + infos[day][1])

    # 현재 날짜의 상담을 진행하지 않는 경우

    dfs(day + 1, sum_price)

dfs(0, 0)
print(answer)
