dwarf = []
for d in range(9):
    dwarf.append(int(input()))

spy = sum(dwarf) - 100
# print(spy)
for x in range(8):
    for y in range(x+1,9):
        if dwarf[x] + dwarf[y] == spy:
            dwarf.pop(y)
            dwarf.pop(x)
            dwarf.sort()
            for i in dwarf:
                print(i)
            exit()

n = []
result = []
for i in range(9):
    n.append(int(input()))

for i in range(9):
    m = n[:i] + n[i+1:]
    for j in range(8):
        k = m[:j] + m[j+1:]
        if (sum(k) == 100):
            result = k

result.sort()
for i in result:
    print(i)
    