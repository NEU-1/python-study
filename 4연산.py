def four(num, start, stack):
    print(num, start, stack)
    if start == end:
        save.append([stack])
    if start > end:
        return False
    
    for i in 연산:
        if i == '*':
            if four(num, start*num, stack):
                stack.append(i)
                return True
        elif i == '+':
            if four(num, start + num, stack):
                stack.append(i)
                return True
        elif i == '-':
            if four(num, start-num, stack):
                stack.append(i)
                return True
        elif i == '/':
            if four(num, start/num, stack):
                stack.append(i)
                return True
    stack.pop()
    return False






num, end = map(int,input().split())

start = num
stack = []
연산 = ['*','+','-','/']
save = []

if num == end:
    print(0)
elif four(num, start, stack):
    print(stack)
else:
    print(-1)
