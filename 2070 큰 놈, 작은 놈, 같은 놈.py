t = int(input())


for i in range(0,t):

    num = list(map(int, input().split()))


    if num[0] > num[1]:
        print(f'#{i+1} >')
    elif num[0] < num[1]:
        print(f'#{i+1} <')
    else:
        print(f'#{i+1} =')
