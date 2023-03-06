def check(save, visited, start, cnt):
    visited[start] = True
    for nxt in save[start]:
        if visited[nxt] == False:
            visited[nxt] = True
            cnt += 1
            cnt = check(save, visited, nxt, cnt)

    return cnt


com = int(input())
line = int(input())
save = [[] for _ in range(com+1)]
visited = [False] * (com+1)
cnt = 0

for _ in range(line):
    y, x = map(int,input().split())
    save[y].append(x)
    save[x].append(y)
# print(save)
check = check(save, visited, 1, cnt)
print(check)

# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]






from sys import stdin

n = int(stdin.readline())
v = int(stdin.readline())

graph = [ [] for _ in range(n+1) ]
visited = [0] * (n+1)

for i in range(v) :
    a, b = map(int, stdin.readline().split())

    graph[a] += [b]
    graph[b] += [a]

def dfs(k) :
    visited[k] = 1

    for nx in graph[k] :
        if visited[nx] == 0 :
            dfs(nx)

dfs(1)
print(sum(visited)-1)