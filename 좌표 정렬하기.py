N = int(input())
save = []
for _ in range(N):
    save.append(tuple(map(int,input().split())))
# save.sort(key=lambda x: (x[0], x[1]))
save.sort()
for s in save:
    print(*s)


import sys

def cond(dot):
    x, y = dot.split()
    return int(x) + int(y)/1000000

dots = sorted(sys.stdin.readlines()[1:], key=lambda x: cond(x))
print(''.join(dots))