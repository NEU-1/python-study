num = []
for i in range(10):
    num.append(int(input())%42)

num_set = set(num)
print(len(num_set))

