node, line, start = map(int,input().split())
save = [[] for _ in range(node+1)]
for _ in range(line):
    a, b = map(int,input().split())
    save[a].append(b)
    save[b].append(a)
for s in save:
    s.sort()
# print(save)

# dfs

visited_dfs = [False] * (node+1)
ppprint = []

def dfs(num):
    if visited_dfs[num]:
        return 
    else:
        visited_dfs[num] = True
        ppprint.append(num)

    for i in save[num]:
        dfs(i)
    return ppprint
    
print(*dfs(start))

from collections import deque

visited = [False] * (node+1)
check = deque()
check.append(start)
visited[start] = True
pppprint = [start]
while check:
    n = check.popleft()
    for i in save[n]:
        if visited[i]:
            continue
        else:
            visited[i] = True
            check.append(i)
            pppprint.append(i)
print(*pppprint)



