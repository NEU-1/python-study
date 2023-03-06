# 에라토네스의 채

check = [0] * 100
for c in range(2, 100+1):
    if check[c] == 0:
        for h in range(c*2, 100+1, c):
            h == 1
    print(c)

# 버블 정렬
save = list(map(int,input().split()))
for n in range(N-1, -1, -1):
    for check in range(0, n):
        if save[check] > save[check+1]:
            save[check], save[check+1] = save[check+1], save[check]

# 카운팅 정렬
num = int(input())
save = [0]*(num+1)
결과 = [0]*(num+1)
목록 = list(map(int,input().split()))
for c in 목록:
    save[c] += 1

for s in range(1, len(save)):
    save[s] += save[s-1]

for e in range(len(목록)-1, -1, -1):
    save[목록[e]] -= 1
    결과[save[목록[e]]] = 목록[e]

# 큌 정렬

def quick(x):
    if len(x) <= 1:
        return x
    point = x[len(x)//2]
    front = []
    back = []
    middle = []
    for a in x:
        if a > x:
            front.append(a)
        elif a < x:
            back.append(a)
        else:
            middle.append(a)
    return quick(front) + middle +quick(back)

# 선택 정렬
for n in range(num):
    mn = n
    for m in range(n+1, num):
        if lis[mn] > lis[m]:
            mn = m
    lis[mn], lis[m] = lis[m], lis[mn]


