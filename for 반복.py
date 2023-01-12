start,finish = input().split()

print(start,finish)

start = int(start)
finish = int(finish)

temp = int(input())

            
while temp != -999:
    if start <= temp <= finish:
        print('Nothing to report')
        temp = int(input())
        
    else:
            print('Alert!')
            break
