'''
Q) 입력에서 요구한 두 사람(a, b)의 촌수를 나타내는 정수를 출력한다
    촌수를 계산할 수가 없을 경우 -1 을 출력한다
'''


def dfs(cur_node, b, depth):
    global answer
    if cur_node == b:
        answer = depth
        return

    for adj_node in adj_list[cur_node]:
        if not visited[adj_node]:
            visited[adj_node] = 1
            dfs(adj_node, b, depth + 1)


# 전체 사람의 수
n = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())
# 부모 자식들 간의 관계의 개수

m = int(input())
# 인접 리스트
adj_list = [[] for _ in range(n + 1)]

# 부모 자식간의 관계를 나타내는 두 번호 x,y
for _ in range(m):
    # x : y 의 부모 번호
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

# 방문 확인을 위한 변수
visited = [0] * (n + 1)
visited[a] = 1

answer = - 1

dfs(a, b, 0)

print(answer)
