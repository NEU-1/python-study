num = int(input())
change = list(map(int, input().split()))

student = list(range(1, num+1))
for n in range(num):
    # print(student.pop(n))
    target = student.pop(n)
    student.insert(n-change[n], target)
    # print(student)

print(*student)



import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
ans = []

for i in range(n):
    ans.insert(i - L[i], i + 1)

print(*ans)