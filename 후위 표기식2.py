N = int(input())
word = list(input())
save = []
stack = []

for n in range(N):
    save.append(int(input()))

for w in word:
    if 'A' <= w <= 'Z':
        stack.append(save[ord(w)-65])
    else:
        a = stack.pop()
        b = stack.pop()
        if w == '*':
            c = b*a
            stack.append(c)
        elif w == '/':
            c = b/a
            stack.append(c)
        elif w == '+':
            c = b+a
            stack.append(c)
        elif w == '-':
            c = b-a
            stack.append(c)

print(f'{stack[0]:.2f}')


