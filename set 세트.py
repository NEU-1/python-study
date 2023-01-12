fruits = {'apple', 'banana', 'orange'}

fruits.add('mango')
print(fruits)

companies = set()
companies = {'apple', 'microsoft', 'google'}

print(companies)

print(type(fruits), type(companies))

a = fruits & companies

b = fruits | companies

print(a)
print(b)


list_of_sets = [fruits, companies]
c = set.intersection(*list_of_sets)
d = set.union(*list_of_sets)

print(c)
print(d)

alphabet = list('google')
print(alphabet)

e = set(alphabet)
print(e)

s1 = {1,2,3,4,5,6,7}
s2 = {1,3,5,7}
s3 = s1 -s2
print(s3)
