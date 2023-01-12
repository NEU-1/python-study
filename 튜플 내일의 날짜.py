t = list(map(int,input().split()))

yyyy = t[0]
mm = t[1]
dd = t[2]

print(f'{mm}/{dd}/{yyyy}')

if dd == 31:
    dd = 0
    mm+=1
if mm == 13:
    mm=1
    yyyy+=1

print(f'{mm}/{dd+1}/{yyyy}')
