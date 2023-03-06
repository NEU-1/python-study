import sys
for _ in range(int(sys.stdin.readline())):
    save = []
    num = int(sys.stdin.readline())
    for _ in range(num):
        save.append(str(sys.stdin.readline().strip()))
    end = 'YES'
    # print(save)
    save.sort()
    
    for s in range(num-1):
        if save[s+1][0:len(save[s])] == save[s]:
            end = 'NO'

    print(end)
