def make(cnt, num, i):
    if cnt == 6:
        print(*save)
        return
    
    for n in range(i, N):
        if num[n] not in save:
            save.append(num[n])
            make(cnt+1, num, n+1)
            save.pop()
    return





while True:
    word = input()
    if word == '0':
        break
    N, *num = map(int, word.split())
    save = []
    num.sort()

    make(0, num, 0)
    print()