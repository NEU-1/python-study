
# def DFS(cnt):
#     if cnt == M:
#         print(' '.join(map(str, save)))
#         return
#     for i in range(1, N+1):
#         if not visited[i]:
#             visited[i] = True
#             save.append(i)
#             DFS(cnt+1)
#             visited[i] = False
#             save.pop()

# N, M = map(int, input().split())
# visited = [False] * (N + 1)
# save = []

# DFS(0)



# def com(num, start, M):
#     if M == 0:
#         print(*num)
#     else:
#         for i in range(start, N+1):
#             com(num + [i], i+1, M-1)

# N, M = map(int, input().split())
# com([], 1, M)



# def com(num, start, M):
#     if M == 0:
#         print(*num)
#     else:
#         for i in range(start, N+1):
#             com(num + [i], 1, M-1)

# N, M = map(int, input().split())
# com([], 1, M)



# def com(num, start, M):
#     if M == 0:
#         print(*num)
#     else:
#         for i in range(start, N+1):
#             com(num + [i], i, M-1)

# N, M = map(int, input().split())
# com([], 1, M)



# def DFS(cnt):
#     if cnt == M:
#         print(' '.join(map(str, save)))
#         return
#     for i in save:
#         if not visited[i]:
#             visited[i] = True
#             save.append(i)
#             DFS(cnt+1)
#             visited[i] = False
#             save.pop()

# N, M = map(int, input().split())
# save = []
# save = list(map(int,input().split()))
# save.sort()
# visited = [False] * (max(save)+1)

# DFS(0)



# def com(num, start, M):
#     if M == 0:
#         print(*num)
#     else:
#         for i in range(start, N):
#             com(num + [save[i]], i+1, M-1)

# N, M = map(int, input().split())
# save = list(map(int, input().split()))
# save.sort()
# com([], 0, M)



# def com(num, save, M):
#     if M == 0:
#         print(*num)
#     else:
#         for i in save:
#             com(num + [i], save, M-1)

# N, M = map(int, input().split())
# save = list(map(int, input().split()))
# save.sort()
# com([], save, M)



# def com(num, start, M):
#     if M == 0:
#         print(*num)
#     else:
#         for i in range(start, N):
#             com(num + [save[i]], i, M-1)

# N, M = map(int, input().split())
# save = list(map(int, input().split()))
# save.sort()
# com([], 0, M)



# N, M = map(int, input().split())
# save = list(map(int, input().split()))
# save.sort()
# lst = []
# cnt = 0
# visited = [False] * (N+1)

# def DFS(depth):
#     prev = 0
#     if depth == M:
#         print(*lst)
#         return
#     else:
#         for i in range(N):
#             if save[i] != prev and visited[i] == False:
#                 lst.append(save[i])
#                 prev = save[i]
#                 visited[i] = True
#                 DFS(depth + 1)
#                 lst.pop()
#                 visited[i] = False

# DFS(0)



# import sys
# input = sys.stdin.readline

# def f(c):
#     if c == m:
#         print(' '.join(ans))
#         return
#     t = -1
#     for j in range(n):
#         if visit[j] or t == ls[j]:
#             continue
#         visit[j] = 1
#         ans.append(ls[j])
#         f(c+1)
#         visit[j] = 0
#         t = ans.pop()

# n, m = map(int, input().split())
# ls = input().split()
# ls.sort(key=int)
# ans, visit = [], [0]*n
# f(0)



# N, M = map(int, input().split())
# save = list(map(int, input().split()))
# save.sort()
# lst = []
# cnt = 0
# visited = [False] * (N+1)

# def DFS(depth, k):
#     prev = 0
#     if depth == M:
#         print(*lst)
#         return
#     else:
#         for i in range(k, N):
#             if save[i] != prev and visited[i] == False:
#                 lst.append(save[i])
#                 prev = save[i]
#                 visited[i] = True
#                 DFS(depth + 1, i)
#                 lst.pop()
#                 visited[i] = False

# DFS(0, 0)



N, M = map(int, input().split())
save = list(map(int, input().split()))
save.sort()
lst = []
cnt = 0
visited = [False] * (N+1)

def DFS(depth, k):
    prev = 0
    if depth == M:
        print(*lst)
        return
    else:
        for i in range(k, N):
            if save[i] != prev:
                lst.append(save[i])
                prev = save[i]
                visited[i] = True
                DFS(depth + 1, i)
                lst.pop()
                visited[i] = False

DFS(0, 0)