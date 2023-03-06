_ = input()
word = list(input())
save = 0
for w in range(len(word)):
    save += (ord(word[w])-96)*(31**w)%1234567891
print(save%1234567891)