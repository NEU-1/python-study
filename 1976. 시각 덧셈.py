T = int(input())
for t in range(1, T+1):
        
    time = list(map(int,input().split()))
    hour = time[0] + time[2]
    minute = time[1] + time[3]

    if minute > 60:
        hour += (minute//60)
        minute %= 60

    if hour > 12:
        hour %= 12

    print(f'#{t} {hour+(hour==0)*12} {minute}')


    for i in range(int(input())):
        a,b,c,d=map(int,input().split())
        e=(a+c+((b+d)>59))%12
        print("#{}".format(i+1),e+(e==0)*12,(b+d)%60)
