num = list(map(int,input().split()))

check = list(range(1, 9))

if num == check:
    print('ascending')
elif num == check[::-1]:
    print('descending')
else:
    print('mixed')