import sys

k = int(sys.stdin.readline())
visit_order = list(map(int, sys.stdin.readline().split()))

# 각 레벨의 노드 개수를 계산합니다.
level_node_count = [2**(i-1) for i in range(1, k+1)]

node_number = 1
for i in range(k):
    # 레벨 i의 노드 개수만큼 반복합니다.
    for j in range(level_node_count[i]):
        # 현재 노드의 번호가 주어진 방문 순서에서 몇 번째에 있는지 계산합니다.
        index = visit_order.index(node_number)

        # 현재 노드의 번호를 출력합니다.
        print(node_number, end=' ')

        # 다음 노드의 번호를 계산합니다.
        if j % 2 == 0:
            node_number = node_number + 2**(k-i-1)
        else:
            node_number = node_number + 1

        # 현재 노드의 방문 순서를 제거합니다.
        visit_order.pop(index)
    print()
