i=0
                    
while i<3:
    year = int(input())


    if year%4 != 0:
        i=1
    elif year%100 != 0:
        i=2
    elif year%400 != 0:
        i=1
    else:
        i=2


    if  i==2:
        print(year,'년은 윤년입니다')
    elif i==1:
        print(year,'년은 평년입니다')




while True:
    is_leap_year = 0

    year = int(input())

    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 ==0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        print(year,'년은 윤년입니다')
    else:
        print(f'{year} 년은 평년입니다')
        
