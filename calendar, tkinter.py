import calendar
c = calendar.TextCalendar()
help(c)
m = c.formatmonth(2021,2)
print(m)


import tkinter as tk

s = 'Life is short\nUse Python'
root = tk.Tk()
t = tk.Text(root, height = 2, width = 13)
t.insert(tk.END, s)
t.pack()

help(root)

import calendar
import tkinter as tk

a = calendar.TextCalendar()
b = a.formatmonth(2021, 3)

d = tk.Tk()
e = tk.Text(d, height = 7, width = 20)
e.insert(tk.END, b)
e.pack()
tk.mainloop()
