import sys

n, m = map(int, sys.stdin.readline().split())

passwords = {}
for i in range(n):
    site, password = sys.stdin.readline().split()
    passwords[site] = password

for j in range(m):
    site = sys.stdin.readline().rstrip()
    print(passwords[site])
