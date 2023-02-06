# import sys

# def two(num):
#     if num <= 1:
#         return str(num)
#     return two(num//2)+ str(num%2)
# # print(two(14))

num, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort
save = 0

for c1 in range(num-2):
    for c2 in range(c1+1, num-1):
        for c3 in range(c2+1, num):
            if card[c1] + card[c2] + card[c3] == M:
                save = M
            elif save < card[c1] + card[c2] + card[c3] < M:
                save = card[c1] + card[c2] + card[c3]

print(save)
# new_card = []
# for c in card:
#     if c < M:
#         new_card.append(c)
# hap = 0
# save = 0

# for i in range(1, 1<<num):
#     # print(list(map(int,two(i))))
#     if list(map(int,two(i))).count(1) == 3:
#         for j in range(num):
#             if i & (1<<j):
#                 hap += new_card[j]
#     # print(count, hap)

#     if hap == M:
#         save = hap
#         break    
#     elif save < hap < M:
#         save = hap

#     hap = 0

# print(save) 



