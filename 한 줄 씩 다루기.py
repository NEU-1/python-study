import os
a = os.getcwd()

b = os.listdir()

print(a,b)

f = open('LICENSE.txt')

c = f.readline()

print(c)

for x in range(5):
    d = f.readline()
    print(d)


f = open('LICENSE.txt')
lines = f.readlines()
e = lines[:2]
print(e, end='')

for i in lines[26:41]:
    print(i, end='')

for l in lines[-5:]:
    print(l, end='')
