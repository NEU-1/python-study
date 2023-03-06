run = int(input())
for r in range(run):
    num, target = map(int,input().split())
    paper = list(map(int,input().split()))
    check = [0]*num
    check[target] = 1
    count = 0

    
    while True:
        if paper[0] == max(paper):
            count += 1
            if check[0] == 1:
                print(count)
                break
            else:
                del paper[0]
                del check[0]
        else:
            paper.append(paper[0])
            del paper[0]
            check.append(check[0])
            del check[0]



# t = int(input())
# for i in range(t):
#     n, m = map(int, input().split())
#     s = list(map(int, input().split()))
#     s_ = [0 for i in range(n)]
#     s_[m] = 1
#     cnt = 0
#     while True:
#         if s[0] == max(s):
#             cnt += 1
#             if s_[0] == 1:
#                 print(cnt)
#                 break
#             else:
#                 del s[0]
#                 del s_[0]
#         else:
#             s.append(s[0])
#             del s[0]
#             s_.append(s_[0])
#             del s_[0]