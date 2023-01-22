import sys

a, b = list(map(int,sys.stdin.readline()split()))
while (a, b) != (0, 0):
    print(a+b)
    a, b = list(map(int,sys.stdin.readline()split()))

import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)