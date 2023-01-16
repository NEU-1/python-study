T = int(input())
for t in range(1, T+1):
    N,K = list(map(int,input().split())) # 범위값 입력
    print(N,K)
    qube = None
    for y in range(N): # 활동범위 설정
        for x in range(N-K+1): # 활동범위 설정
            qube = [list(map(int,input().split())) for z in range(N)] 
            # 큐브 완성
            count = 0
            plus = 0
            for i in range(K):
                if qube[y][x+i] == True:
                    count += 1
            if count == K:
                plus += 0
    for y in range(N-K+1): # 활동범위 설정
        for x in range(N): # 활동범위 설정
            qube = [list(map(int,input().split())) for m in range(N)] 
            # 큐브 완성
            count = 0
            plus = 0
            for i in range(K):
                if qube[y][x+i] == True:
                    count += 1
            if count == K:
                plus += 0



    print(f'{t} ')