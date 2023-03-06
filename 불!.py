from collections import deque

def run(save):
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]

    while save:
        y, x, a = save.popleft()
        # print(y,x,a)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if type(a) == int:
                if ny <0 or nx < 0 or ny >= R or nx >= C:
                    return a+1
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            if maze[ny][nx] == '#' or visited[ny][nx]:
                continue
            if maze[ny][nx] == 'J' or maze[ny][nx] == '.':
                # print(ny,nx, save)
                visited[ny][nx] = True
                if type(a) == int:
                    save.append((ny,nx,a+1))
                else:
                    save.append((ny,nx,a))
    
    return 'IMPOSSIBLE'


R, C = map(int,input().split())

maze = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
save = deque()
ji = []
for y in range(R):
    for x in range(C):
        if maze[y][x] == 'J':
            ji.append((y,x,int(0)))
        elif maze[y][x] == 'F':
            save.append((y,x,'f'))
            visited[y][x] = True
save.append(ji.pop())
# print(save)
end = run(save)

print(end)