T = int(input())
for t in range(1, T+1):
    N = int(input())
    색종이 = set()
    for _ in range(N):
        x1, y1, x2 , y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        색종이.update(set([(y,x) for x in range(x1,x2+1) for y in range(y1, y2+1)]))
    print(f'#{t} {len(색종이)}')