import os
os.getcwd()
line = open('postcard.txt','r').read()

a, b, c = tuple(line.split('\n\n'))
print('\n' + b + '\n')

d = b.replace(',','')
b = d.replace('.','')
d = b.replace(':','')
print('\n' + d + '\n')

e = d.upper()
print('\n' + e + '\n')

f = []
for i in e.split('\n'):
    f += i.split()[:2]
print(' '.join(f))
