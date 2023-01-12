N = int(input())

a = []
a=list(map(int,input().split()))


a.sort()

b = int(((N+1)/2)-1)

print(a[b])
      
