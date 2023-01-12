num = int(input())
result = str(num)

if num >= 1000:
    result = str(num//1000)+'k'
elif num>= 0:
    pass

print (result)



num=int(input())

result = str(num)

if num >= 1000000:
    result = str(1000000//100000)+'m'
    print(result)
    
