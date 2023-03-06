num = int(input())
fibo = [0]*91
fibo[0] = 0
fibo[1] = 1
for f in range(2, 91):
    fibo[f] = fibo[f-1] + fibo[f-2]
print(fibo[num])