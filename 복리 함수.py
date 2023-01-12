p=int(input('원금:'))
r=float(input('연이율:'))
t=int(input('기간:'))
n=eval(input('복리 횟수:'))

def computnd_interest_amount():

    a=p*(1+r/n)**(n*t)

    return a

computnd_interest_amount()
