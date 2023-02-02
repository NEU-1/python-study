N = int(input())
qube = [[0]*100]*100
# print(qube)
for n in range(N):
    x, y = map(int,input().split())
    for plus_y in range(10):
        qube[y+plus_y] = qube[y+plus_y][:x] + [1]*10 + qube[y+plus_y][x+10:]
count = 0
for i in qube:
    count += i.count(1)

print(count)




import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(n):
    w, h = map(int, input().split())
    
    for j in range(w, w+10):
        for k in range(h, h+10):
            arr[j][k] = 1

ans = 0
for i in arr:
    ans += sum(i)
print(ans)