a = input()
num = sum(map(int,list(input())))
print(num)


a, b = list(map(int, input().split()))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)



while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
