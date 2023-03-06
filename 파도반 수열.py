sam = [0] * 101
sam[1] = 1
sam[2] = 1
sam[3] = 1
sam[4] = 2
sam[5] = 2
for s in range(5,101):
    sam[s] = sam[s-1] + sam[s-5]
for _ in range(int(input())):
    print(sam[int(input())])



import sys
input = sys.stdin.readline

pad = [1,1,1,2,2]

for i in range(95):
    pad.append(pad[-1] + pad[-5])

for _ in range(int(input())):
    M = int(input())
    print(pad[M-1])