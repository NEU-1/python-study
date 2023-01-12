t = int(input())

for i in range(0,t):
    
    a = int(input())

    yyyy = a//10000
    mm = (a//100)%100
    dd = a%100

    if yyyy!= 0000:
        if mm in (1,3,5,7,8,10,12):
            if dd>0 and dd<32:
                print(f'#{i+1} {yyyy:>4}/{mm:0>2}/{dd:0>2}')
            else:
                print(f'#{i+1} -1')
        elif mm in (4, 6, 9, 11):
            if dd>0 and dd<31:
                print(f'#{i+1} {yyyy:>4}/{mm:0>2}/{dd:0>2}')
            else:
                print(f'#{i+1} -1')
        elif mm == 2:
            if dd>0 and dd<29:
                print(f'#{i+1} {yyyy:>4}/{mm:0>2}/{dd:0>2}')
            else:
                print(f'#{i+1} -1')
        else:
            print(f'#{i+1} -1')
                

