T = int(input())
for t in range(1, T+1):
    N = int(input())
    산 = [list(map(int,input().split())) for n in range(N)]
    save = []
    for y in range(1, N-1):
        for x in range(1, N-1):
            cnt = 0
            for _y, _x, in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                if 산[y][x] > 산[y+_y][x+_x]:
                    cnt += 1
            if cnt == 4:
                save.append(산[y][x])
    # 카운팅 정렬
    mid = [0] * (max(save)+1)
    end = [0]*len(save)
    # print(end)
    for s in save:
        mid[s] += 1
    for m in range(1, len(mid)):
        mid[m] += mid[m-1]
    # print(mid)
    for a in range(len(save)-1, -1, -1):
        mid[save[a]] -= 1
        end[mid[save[a]]] = save[a]
        # print(mid[save[a]])

    print(f'#{t} {end[0]} {end[-1]}')


                    
            
