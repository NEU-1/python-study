def su(a):
    if a == 0:
        return 0
    return a + su(a-1)
count = 0
run = int(input())
# print(su(10))
for i in range(run):
    b = list(input().split('X'))
    # print(b)
    for j in b:
        # print(su(len(j)))
        count += su(len(j))
    print(count)
    count = 0



import sys

for _ in range(int(sys.stdin.readline())):
    point = 0
    for x in str(sys.stdin.readline())[:-1].split('X'):
        point += len(x)*(len(x)+1)//2
    print(point)