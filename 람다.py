def hap(x,y):
    return x+y

print(hap(10,20))


print((lambda x,y: x+y)(10,20))


b=map(lambda a: a**2, range(5))

print(list(b))



from functools import reduce
print(reduce(lambda z, v: z+v, [0, 1, 2, 3, 4, 5]))


print(reduce(lambda n, m:m+n, 'abcde'))


i=filter(lambda x: x<5, range(10))
print(list(i))


o = filter(lambda x:(x+1)%2, range(10))
print(list(o))


