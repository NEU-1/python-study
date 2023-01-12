dice1 = (1,2,3,4,5,6)
dice2 = (2,3,5,7,11,13)
num = []

for i in range(6):
    a = dice1[i]
    for l in range(6):
        b = dice2[l]
        c=(a+b)
        num.append(c)
    
num.sort()
print(set(num))
