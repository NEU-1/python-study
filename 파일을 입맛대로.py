users = {'kim':'3kid9', 'sun80':'393948','1jm':'py90390'}
f = open('users', 'wb')
import pickle
pickle.dump(users, f)
f.close()

import os
os.path.exists('users')

f = open('users', 'rb')
a = pickle.load(f)
print(a)


from glob import glob
glob('*,exe')
glob('*.txt')

glob(r'C:\u*')

from glob import glob
from os.path import isdir

for x in glob('*'):
    if isdir(x):
        print(x, '<DIR>')
    else:
        print(x)
