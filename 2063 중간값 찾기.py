n = int(input())

num = list(map(int,input().split()))

h = int((n-1)/2)

num.sort()

print(num[h])
