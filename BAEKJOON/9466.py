T = int(input())


def dfs(cur_node, visited):
    global answer

    # 현재 노드에서 바라보는 노드
    next_node = grpah[cur_node]

    # 현재 노드에서 바라보는 노드가 이미 팀이 완성된 경우 -> 현재 노드는 팀이 만들어질 수 없음
    if checks[next_node]:
        return

    # 팀 조합이 가능한 경우들(현재 노드가 선택하길 희망하는 노드와 시작노드가 동일)
    if next_node == visited[0]:
        answer += len(visited)
        for node in visited:
            checks[node] = True
        return

    if next_node not in visited:
        dfs(next_node, visited + [next_node])

    # 실패한 경우
    for i in range(len(visited)-1):
        checks[visited[i]] = True




for _ in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    checks = [False] * (n + 1)
    grpah = [[] for _ in range(n + 1)]

    for idx, number in enumerate(numbers):
        grpah[idx + 1] = number

    answer = 0
    for node in range(1, n + 1):
        # 팀 구성이 완료되지 않은 노드만 DFS 시행
        if not checks[node]:
            dfs(node, [node])
    answer = n - answer
    # print(checks)
    print(answer)
