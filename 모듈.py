import math

a = math.sqrt(2)

print(a)

b = math.sqrt(3)

print(b)

c = math.sqrt(4)

print(c)

d = math.pi

print(d)

import calendar

e = calendar.prmonth(2013, 7)

print(e)

from tkinter import *
widget = Label(None, text = 'i love python!')
widget.pack()

print(dir(tkinter))

import tkinter
tkinter.widget = tkinter.label(None, text = 'i love python!')
tkinter.widget.pack()


del tkinter
from importlib import reload
reload('모듈')
