num = list(map(int,input().split()))
p = num[0]
k = num[1]


if p > k:
    print(p-k+1)
else:
    print(p-k+1000)
