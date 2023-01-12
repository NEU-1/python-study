t = int(input())

for i in range(t):
    a=list(map(int,input().split()))
    b=[]
    b.append(a[0]//a[1])
    b.append(a[0]%a[1])
    print(f'#{i+1} {b[0]} {b[1]}')
    
