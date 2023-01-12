
def palindrome(word):
    word = word.replace(' ', '').lower()
    return word == word[::-1]





word = input()



print(palindrome(word))
