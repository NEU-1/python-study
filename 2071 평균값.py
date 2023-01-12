t = int(input())


for i in range(0,t):

    num = list(map(int, input().split()))


    b = round(sum(num)/10)

    print (f'#{i+1} {b}')
