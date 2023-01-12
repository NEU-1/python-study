dic = {}
dic['dictionary'] = '1. A'
dic['python'] = 'Any'
dic['dictionary']

print(dic)
print(dic['dictionary'])

smalldic = {'dictionary': 'reference', 'python': 'snake'}
print(smalldic)
print(smalldic['python'])

del smalldic['dictionary']
print(smalldic)


family = {'boy':'choi','girl':'kim','baby':'choi'}
print(family)
family.keys()
family.values()

print(family.keys())
print(family.values())

print('boy' in family)

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7]
print(list1+list2+list3)

