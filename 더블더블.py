num = int(input())
two = 1
end = []
for i in range(1, num+2):
    end.append(two)
    two = 2**i
    

print(*end)
