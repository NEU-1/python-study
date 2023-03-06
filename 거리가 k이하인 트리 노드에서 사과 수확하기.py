def dfs(save, visited, start, down):
    if down == 2:
        return True

    visited[start] = True

    for nxt in save[start]:
        if visited[nxt] == False:
            visited[nxt] = True
            down += 1
            r = dfs(save, visited, nxt, down)
            if r == True:
                return True
            down -= 1
    return False





nod, k = map(int, input().split())

save = [[] for _ in range(nod)]
visited = [False] * nod
down = 0
for _ in range(nod-1):
    y, x = map(int, input())
    save[y].append(x)

apple = list(map(int, input().split()))

