import sys
input = sys.stdin.readline

n,m = map(int,input().split())

qube1 = [list(map(int, input().split())) for i in range(n)]
qube2 = [list(map(int, input().split())) for i in range(n)]

for y in range(n):
    for x in range(m):
        # print(qube[y][x])
        qube1[y][x] += qube2[y][x]
    print(*qube1[y])