
def read(text):
    ridename, cm = map(str.strip, text.split(':'))

    cmmin = cmmax = None

    if '~' in cm:
        cmmin, cmmax = map(lambda x: int(x.replace('cm','')), cm.split('~'))
    elif '이상' in cm:
        cmmin = int(cm.split('cm')[0])

    return ridename, cmmin, cmmax

text = input()

if __name__ == "__main__":  
    ridename, cmmin, cmmax = read(text)

    print('이름: ', ridename)
    print('하한: ', cmmin)
    print('상한: ', cmmax)
