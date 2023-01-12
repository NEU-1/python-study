
def gugu():
    for i in range(2,10):
        for n in range(1,10):
            print(f'{i} * {n} = {i*n:2d}')

gugu()



a = int(input())

def gugu(a):
    for i in range(1,10):
            print(f'{i} * {a} = {i*a:2d}')
print(gugu(a))



def multi(m):
    for n in range(1, 10):
        print(f'{m} * {n} = {m*n:2d}')
        

if __name__ == '__main__':
    for i in range(2, 10):
        multi(i)
        print()
