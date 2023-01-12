score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]
print(score)

stem_leaf = [[], [], []]
for s in score:
    d, m = divmod(s,10)
    stem_leaf[d].append(m)

print(stem_leaf)
print(stem_leaf[0])
print(stem_leaf[1])
print(stem_leaf[2])

for i in range(len(stem_leaf)):
    print(f'{1}: {stem_leaf[i]}')


