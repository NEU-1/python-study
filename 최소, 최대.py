a = input()
num = list(map(int, input().split()))
max_num = max(num)
min_num = min(num)

print(min_num, max_num)



from sys import stdin
_, *a = map(int, stdin.buffer.read().split())
print(min(a), max(a))