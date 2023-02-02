x, y = map(int, input().split())
num = int(input())
x_list = []
y_list = []
for n in range(num):
    a, b = map(int, input().split())
    if a == 0:
        y_list.append(b)
    else:
        x_list.append(b)
x_list.append(x)
y_list.append(y)
x_list.sort()
y_list.sort()
# print(y_list)
x_save = [x_list[0]]
y_save = [y_list[0]]
for i in range(1, len(x_list)):
    x_save.append(x_list[i]-x_list[i-1])
for j in range(1, len(y_list)):
    y_save.append(y_list[j]-y_list[j-1])
print(max(x_save) * max(y_save))




w,h = map(int,input().split())
W = [w,0]
H = [h,0]
T = int(input())

for i in range (0,T):
  d, n = map(int,input().split())
  if d == 0:
    H.append(n)
  if d == 1:
    W.append(n)

W.sort()
H.sort()

width=[]
for i in range (1,len(W)):
  for j in range (1,len(H)):
    width.append((W[i]-W[i-1]) * (H[j]-H[j-1]))

print(max(width))