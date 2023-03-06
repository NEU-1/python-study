def sell(lst, mid):
    money = 0
    for i in range(mid):
        money += sum(lst[i][mid-i:mid+1+i])
        # print(lst[i][mid-i:mid+1+i])
    return money

T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int,list(str(input())))) for _ in range(N)]
    # print(farm)
    mid = N//2
    up = farm[:mid]
    down = farm[mid+1:][::-1]
    middle = farm[mid]
    money = 0
    money = sell(up, mid) + sum(middle) + sell(down, mid)
    print(f'#{t} {money}')