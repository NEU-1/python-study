import sys
input = sys.stdin.readline
n = int(input())
room = []
for i in range(n):
    start, end = map(int, input().split())
    room.append((start, end))

room = sorted(room, key=lambda x: (x[1], x[0]))
cnt = 0
check = 0
for start, end in room:
    if start >= check:
        cnt += 1
        check = end
print(cnt)
