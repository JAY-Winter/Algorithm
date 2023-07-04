
node_dict = {}

N = int(input())
for i in range(N):
    node, left, right = input().split()
    if node_dict.get(node):
        pass
    else:
        node_dict[node] = ['.'] * 3
        node_dict[node][0] = i
        node_dict[node][1] = left
        node_dict[node][2] = right
print(node_dict)

visited = []
def search(node):
    if node == '.':
        return
    
    print(node, end='')
    
    visited.append(node)
    for nodes in node_dict[node]:
        nodes = str(nodes)
        if not nodes.isalpha():
            continue
        
        if nodes not in visited:
            search(nodes)

search('A')
# print(node_dict['A'])