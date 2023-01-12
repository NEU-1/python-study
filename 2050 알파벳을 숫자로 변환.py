a = input()
b = []


for i in range(len(a)):
    b.append(ord(a[i])-64)
    
print(" ".join(map(str,b)))



