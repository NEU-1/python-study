save = []
for four in range(4):
    x, y, x1, y1 = map(int,input().split())
    for Y in range(y,y1):
        for X in range(x,x1):
            # save.append(str(X)+str(Y))
            save.append((X,Y))
print(save)
save = set(save)
# print(save)
print(len(save))



r=[]
for i in open(0):
    a,b,c,d=map(int,i.split())
    r+=[(x,y)for x in range(a,c)for y in range(b,d)]
print(len(set(r)))
