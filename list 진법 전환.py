a = int(input())
b = []

while a>0:

    b.append(divmod(a,2)[1])
    a = divmod(a,2)[0]
    print(a,b)

