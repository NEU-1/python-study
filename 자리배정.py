max_x, max_y = map(int,input().split())
ticket = int(input())
qube = [[0 for x in range(max_x)] for y in range(max_y)]
# print(qube)
if ticket > max_x * max_y:
    print(0)
else:
        
    seat = 1
    start_x, end_x = 0, max_x - 1
    start_y, end_y = 0, max_y - 1

    while seat <= max_y * max_x:
        for y_up in range(start_y, end_y+1):
            if seat == ticket:
                print(start_x+1, y_up+1)
                exit()
            qube[y_up][start_x] = seat
            seat += 1
        start_x += 1
        
        for x_up in range(start_x, end_x+1):
            if seat == ticket:
                print(x_up+1, end_y+1)
                exit()
            qube[end_y][x_up] = seat
            seat += 1
        end_y -= 1
        
        for y_down in range(end_y, start_y-1, -1):
            if seat == ticket:
                print(end_x+1, y_down+1)
                exit()
            qube[y_down][end_x] = seat
            seat += 1
        end_x -= 1
        
        for x_down in range(end_x, start_x-1, -1):
            if seat == ticket:
                print(x_down+1, start_y+1)
                exit()
            qube[start_y][x_down] = seat
            seat += 1
        start_y += 1






import sys;
sys.setrecursionlimit(10**7)

def f(c, r, n):
    if c*r<n:
        return 0,
    if n<=r:
        return 1, n

    x, y = f(r, c-1, n-r)
    return 1+y, r-x+1

c, r = map(int, input().split())
n = int(input())
print(*f(c, r, n))