y, x = map(int,input().split())
snake = 0
if y%2 == 1 and x%2 == 1:
    snake = y*x-1
else:
    snake = y*x
print(snake)
