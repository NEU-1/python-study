import string
string.ascii_lowercase

string.ascii_uppercase[3:] + string.ascii_uppercase[:3]

tt = str.maketrans(string.ascii_lowercase, string.ascii_uppercase[3:] + string.ascii_uppercase[:3])

a = input()

b = a.translate(tt)

print(b)
