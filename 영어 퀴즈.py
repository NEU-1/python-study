

import random

dic = dict()

with open('ko en.txt') as f:
    for line in f.readlines()[1:]:
        k, v = tuple(line.split('\t'))
        dic[k] = v

quiz = list(dic.keys())
random.shuffle(quiz)

print(quiz)

while True:
    if len(quiz) == 0:
        break

    q = quiz.pop()
    print('write the following sentence in English.')
    print(q)
    a = input('\nyour answer: ')

    if a == dic[q].rstrip():
        print('\nresult: Correct!')
    else:
        print('\nresult: Not correct!')
        print('right answer:' + dic[q].rstrip() + '\n')

    input()

    print('-' * 80)
        
