t = int(input())


for i in range(0,t):

    num = list(map(int, input().split()))


    b = 0

    for l in range(0,10):
        if num[l]%2 == 1:
            b = b+num[l]
    print(f'#{i+1} {b}')

