t = int(input())


for i in range(0,t):

    num = list(map(int, input().split()))


    num.sort()
    print(f'#{i+1} {num[9]}')
