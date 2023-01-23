num = []
cal = 0
for i in range(3):
    num.append(int(input()))

a = num[0]*num[1]*num[2]
# print(a)
a_list = map(int, list(str(a)))
# print(a_list)
coun = dict()
for i in range(0, 10):
    coun.setdefault(i,0)

# print(coun)
for j in a_list:
    # print(j)
    # print(coun[j])
    coun[j] += 1
# print(coun)
for n in coun.values():
    print(n)



b = int(input()) * int(input()) * int(input())

for i in range(10):
  print(str(b).count(str(i)))