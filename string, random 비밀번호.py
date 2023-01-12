import string

a = string.ascii_uppercase
print(a)


b = string.ascii_lowercase
print(b)

c = string.ascii_letters
print(c)

d = string.digits
print(d)

alphanumeric = c + d
print(alphanumeric)

e = len(alphanumeric)
print(e)

f = list(set(alphanumeric) - set('lio0')) + ['_']
print(f)

g = len(f)
print(g)


import random

h = random.choice(f)
print(h)

pw = str()
for i in range(16):
    pw += random.choice(f)

print(pw)
