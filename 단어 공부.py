import collections
word = list(input().upper())
a = dict(collections.Counter(word))
save = []

for i, j in a.items():
    if j == max(a.values()):
        save.append(i)
if len(save) > 1:
    print('?')
else:
    print(*save)