import calendar
print(dir(calendar))

a = [x for x in dir(calendar) if 'leap' in x]
print(a)

b = help(calendar.isleap)

c = calendar.isleap(2077)
print(c)
