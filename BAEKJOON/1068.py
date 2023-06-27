import sys
sys.setrecursionlimit(100005)

N = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())

adj = [[] for _ in range(N)]

for child, parent in enumerate(nodes):
    if parent != -1:

        adj[parent].append(child)

# 여기가 없어서 틀렸었음
if nodes[del_node] != -1:
    adj[nodes[del_node]].remove(del_node)

print(adj)
cnt = 0



def dfs(node):
    global cnt, del_node
    
    if node == del_node:
        return
    
    if len(adj[node]) == 0:
        cnt += 1
        return
    else:
        for adj_node in adj[node]:
            if adj_node != del_node:
                dfs(adj_node)

for idx, node in enumerate(nodes):
    if node == -1:
        dfs(idx)

print(cnt)