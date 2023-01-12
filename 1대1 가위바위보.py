num = list(map(int,input().split()))


if num[0] == 1 and num[1] == 3:
    print('A')
elif num[0] == 3 and num[1] == 1:
    print('B')
elif num[0] > num[1]:
    print('A')
else:
    print('B')
    
    
