f = open('C:/Users/서지호/AppData/Local/Programs/Python/Python311/Python_for_Fun.txt')
print(f.read())


buffer = f.read()
print(buffer)


letter = open('C:/Users/서지호/AppData/Local/Programs/Python/Python311/letter.txt','w')
letter.write('Dear Father,')
letter.close()

letter = open('C:/Users/서지호/AppData/Local/Programs/Python/Python311/letter.txt')
print(letter.read())


letter = open('C:/Users/서지호/AppData/Local/Programs/Python/Python311/letter.txt','a+')
letter.write('\n\nHow are you?')
letter.close()

letter = open('C:/Users/서지호/AppData/Local/Programs/Python/Python311/letter.txt')
print(letter.read())
