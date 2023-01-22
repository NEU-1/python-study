n, x = map(int,input().split())
num = list(map(int,input().split()))
save = []
# print(n,x)
for i in num:
    if i < x:
        save.append(i)
print(*save)
