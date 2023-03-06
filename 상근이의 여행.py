# from collections import deque

# for _ in range(int(input())):
    # N, M = map(int,input().split())
    # airplane = [[] for _ in range(N+1)]
    # visited = [False] * (N+1)
    # for _ in range(M):
        # a, b = map(int,input().split())
    #     airplane[a].append(b)
    #     airplane[b].append(a)

    # save = deque()
    # save.append(a)
    # visited[a] = True
    # cnt = 0

    # while save:
    #     num = save.popleft()

    #     for i in airplane[num]:
    #         if not visited[i]:
    #             visited[i] = True
    #             save.append(i)
    #             cnt += 1
    # print(cnt)

for _ in range(int(input())):
    N, M = map(int,input().split())
    for _ in range(M):
        _ = input()

    print(N-1)