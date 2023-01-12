import math
print(dir(math))

a = math.sqrt(3**2 + 4**2)
print(a)

x = int(input())
y = int(input())
        
def hypotenuse(x,y):
    b = math.sqrt(x**2 + y**2)

    return round(b,2)

print(hypotenuse(x,y))
