import sys
sys.stdin = open("D:/Downloads/input (3).txt", "r")

T = int(input())
sum_q = 0
qube = [list(map(int,input().split())) for z in range(90)]
for t in range(0,90,9):
    count = 0   
    for y in range(0,9,3):
        for x in range(0,9,3):
            for n in range(3):
                for m in range(3):
                    sum_q += qube[y+m+t][x+n]
            if sum_q == 45:
                count += 1
            sum_q = 0
    for z in range(9):
        sum_q += sum(qube[z+t])
        if sum_q == 45:
            count += 1
        sum_q = 0
    for l in range(9):
        for i in range(9):
            sum_q += qube[i+t][l]
        if sum_q == 45:
            count += 1
        sum_q = 0

    print(f'#{int(t/9)+1} {int(count==27)}')


    for t in range(int(input())):
        M=[[*map(int,input().split())]for _ in [0]*9]
        M+=list(zip(*M))
        a=0
        for i in range(3):
            for j in range(3):M+=[sum([M[3*i+p][3*j:3*j+3] for p in range(3)],[])]
        for i in M:
            if sum(i)!=45:
                break
            else:
                a=1
        print("#%d"%(t+1),a)