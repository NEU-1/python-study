num = int(input())
end = []

for i in range(0,num+1):
    end.append(i)

end.sort(reverse=True)
print(*end)
