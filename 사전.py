dic = {}
dic['dictionary'] = '1. A'
dic['python'] = 'Any'
dic['dictionary']

print(dic)
print(dic['dictionary'])

smalldict = {'dictionary': 'reference', 'python': 'snake'}
print(smalldict)
print(smalldict['python'])

del smalldict['dictionary']
print(smalldict)


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

