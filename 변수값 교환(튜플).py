a = 10
b = 20
print (a,b)

temp = a
a=b
b=temp
print (a,b)
c=10
d=20
e = 30
print(c,d,e)
c,d,e = d,c,e
print(c,d,e)


a_magu_print = (1,2,3,4,5,6,7,8,9,10)

def magu_print(x, y, rest):
    print(x, y, rest)

print(a_magu_print)

empty = ()

one = 5,

print(one)

p = (1,2,3)
q = p[:1] + (5,) + p[2:]
print(p,q)

r = p[:1] + (5,) + p[2:]
print(r)

p = (1,2,3)

q = list(p)
print(q)

r = tuple(q)
print(r)
