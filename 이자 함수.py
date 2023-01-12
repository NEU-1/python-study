p = int(input('원금:'))
r = float(input('단리 이율:'))
t = eval(input('기간:'))



def simple_interest():

    a = p*r*t

    return a

print(simple_interest())



def simple_interests():

    b = p*(1+r*t)

    return b

print(simple_interests())

