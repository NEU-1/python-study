def 수열(count):
    if count == N:
        return save
    for c in range(1,4):
        if check(c, count):
            save[count] = c
            if 수열(count+1):
                return save
            save[count] = 0
    return False



def check(c, count):
    save[count] = c
    for a in range(0, count):
        for b in range(1, min(a+2, count-a+1)):
            if save[a-b+1:a+1] == save[a+1:a+b+1]:
                save[count] = 0
                return False
    
    return True



N = int(input())
save = [0]*N
result = 수열(0)
for r in range(N):
    print(result[r], end ='')


