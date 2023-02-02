num = int(input())
for n in range(num):
    _, *a = map(int, input().split())
    _, *b = map(int, input().split())

    if a.count(4) > b.count(4):
        print('A')
    elif  a.count(4) < b.count(4):
        print('B')
    elif a.count(3) > b.count(3):
        print('A')
    elif  a.count(3) < b.count(3):
        print('B')
    elif a.count(2) > b.count(2):
        print('A')
    elif  a.count(2) < b.count(2):
        print('B')
    elif a.count(1) > b.count(1):
        print('A')
    elif  a.count(1) < b.count(1):
        print('B')
    else:
        print('D')
