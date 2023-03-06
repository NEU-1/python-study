def cnt_node(node, tree, del_node):
    # 현재 노드가 삭제할 노드인 경우 0을 반환
    if node == del_node:
        return 0
    
    count = 0
    # 자식 노드들을 재귀적으로 탐색하면서, 남은 노드들의 개수를 세어 누적
    for child in tree[node]:
        count += cnt_node(child, tree, del_node)
            
    # 자식 노드들의 개수가 0이면 리프 노드이므로 1을 반환
    if count == 0:
        return 1
    
    return count


N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
tree = [[] for _ in range(N)]
root = None

# 부모 노드가 없는 노드를 찾아서 이를 루트 노드로 지정
for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

# 루트 노드가 삭제할 노드인 경우 0을 출력
if root == del_node:
    print(0)
else:
    # 루트 노드부터 시작하여, 남은 노드의 개수를 세어 출력
    print(cnt_node(root, tree, del_node))
