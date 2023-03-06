
from collections import deque

N, M = map(int, input().split())

# 인접 리스트를 저장할 리스트 생성
save = [[] for _ in range(N+1)]

# 그래프 정보를 인접 리스트에 저장
for _ in range(M):
    a, b = map(int, input().split())
    save[a].append(b)
    save[b].append(a)

# 케빈 베이컨의 수를 계산할 리스트
people = []

# 모든 노드에 대해 최소 거리를 구하고 케빈 베이컨의 수를 계산
for i in range(1, N+1):
    # BFS 알고리즘을 사용하여 최소 거리를 구함
    jump = [-1 for _ in range(N+1)]
    jump[i] = 0
    queue = deque([i])
    while queue:
        curr = queue.popleft()
        for nxt in save[curr]:
            if jump[nxt] == -1:
                jump[nxt] = jump[curr] + 1
                queue.append(nxt)
    
    # 케빈 베이컨의 수 계산
    people.append(sum(jump[1:]))

# 케빈 베이컨의 수가 가장 작은 사람의 번호 출력
print(people.index(min(people)) + 1)
