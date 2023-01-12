

def palindrome(word):
    backword = (lambda x: x[::-1])(word)

    return backword



word = input()



if palindrome(word) == word:
    print('True')
else:
    print('False')






def palindrome(word):
    backword = word[::-1]

    return backword



word = input()



if palindrome(word) == word:
    print('True')
else:
    print('False')
