s='hello python!'
print(s.find('p'))

h = s[0:6]

print(h)

print(h.rstrip())


print(s.split())
print(s.split()[1])

prime = [3, 7, 11]
prime.append(5)
prime.sort()
prime.insert(0,2)
del prime[4]
a=prime.pop(2)
prime[0] = 1
print(prime)
print(a)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0])


my_int = 123
print(type(my_int))
my_int = str(my_int)
print(type(my_int))


one_to_ten = list(range(1,11))

print(one_to_ten)

sum(one_to_ten)
print(sum(one_to_ten))

chulsu = [90, 85, 70]
kim = [88, 79, 92]

students = [chulsu, kim]
for scores in students:
    print(scores)
    total = 0
    for s in scores:
        total = total + s
    average = total / 3
    print(scores, total, average)
