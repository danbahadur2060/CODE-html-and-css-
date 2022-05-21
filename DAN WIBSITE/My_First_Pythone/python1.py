from cgitb import text
from os import times_result
from tkinter import *
from time import *
def update():
    times_string = strftime("%I:%M:%S %p ")
    time_label.config(text=times_string)
    day_string = strftime("%A")
    day_label.config(text= day_string)
    date_string = strftime("%B %d,%Y")
    day_label.config(text= day_string)
    window.after(1000,update)

    