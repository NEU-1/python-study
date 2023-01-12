num = int(input())
a = [1,num]
for i in range(2,num):
    if num%i == 0:
        a.append(i)
a.sort()
b=tuple(a)

print(b)
        
