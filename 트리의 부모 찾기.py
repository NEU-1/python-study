import sys
sys.setrecursionlimit(10**6)

def check(n):
    for i in save[n]:
        if parents[i] == 0:
            parents[i] = n 
            check(i)

num = int(sys.stdin.readline())

save = [[] for _ in range(num + 1)]
parents = [0] * (num + 1)
parents[1] = 1

for i in range(num - 1):
    a, b = map(int, sys.stdin.readline().split())
    save[a].append(b) 
    save[b].append(a)

check(1)

for i in range(2, num + 1):
    print(parents[i])
