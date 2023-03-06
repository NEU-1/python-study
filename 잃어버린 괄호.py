word = input()

num = []
i = 0
while i < len(word):
    if word[i] in ['+', '-']:
        num.append(word[i])
        i += 1
    else:
        j = i
        while j < len(word) and word[j] not in ['+', '-']:
            j += 1
        num.append(word[i:j])
        i = j

result = 0
save = 0
minus = False
for token in num:
    if token == '+':
        if minus:
            result -= save
        else:
            result += save
        save = 0
    elif token == '-':
        if minus:
            result -= save
        else:
            result += save
        save = 0
        minus = True
    else:
        save += int(token)

if minus:
    result -= save
else:
    result += save

print(result)
