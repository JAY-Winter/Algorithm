from collections import deque


def bfs(n):
    visited = [False] * (n + 1)
    q = deque([(n, 0)])

    while q:
        curr, cnt = q.popleft()

        if curr == 1:
            return cnt

        if visited[curr]:
            continue

        visited[curr] = True

        if curr % 3 == 0:
            q.append((curr // 3, cnt + 1))
        if curr % 2 == 0:
            q.append((curr // 2, cnt + 1))
        q.append((curr - 1, cnt + 1))


N = int(input())


# print(bfs(N))


def min_steps(n):
    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    return dp[n]


print(min_steps(N))
