num = int(input())
fin = []
for i in range(1,num+1):
    if num % i == 0:
        fin.append(i)
print(*fin)
