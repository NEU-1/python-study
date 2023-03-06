def VLR(node, tree):
    if node != '.':
        print(node, end="")
        VLR(tree[node][0], tree)
        VLR(tree[node][1], tree)

def LVR(node, tree):
    if node != '.':
        LVR(tree[node][0], tree)
        print(node, end="")
        LVR(tree[node][1], tree)

def LRV(node, tree):
    if node != '.':
        LRV(tree[node][0], tree)
        LRV(tree[node][1], tree)
        print(node, end="")

# 입력 받기
N = int(input())
tree = {}

# 이진 트리 구성
for i in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

# 전위 순회
VLR('A', tree)
print()

# 중위 순회
LVR('A', tree)
print()

# 후위 순회
LRV('A', tree)
print()
