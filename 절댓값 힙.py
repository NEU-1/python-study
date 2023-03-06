import sys
input = sys.stdin.readline
import heapq

num = int(input())
hip = []
for _ in range(num):
    n = int(input())
    if n != 0:
        heapq.heappush(hip,(abs(n),n//abs(n)))
    elif n == 0:
        if len(hip) == 0:
            print(0)
        else:
            a,b = heapq.heappop(hip)
            print(a*b)


# n = int(input())
# heap = []
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         if len(heap) == 0:
#             print(0)
#         else:
#             print(-heapq.heappop(heap))
#     else:
#         heapq.heappush(heap, -x)
