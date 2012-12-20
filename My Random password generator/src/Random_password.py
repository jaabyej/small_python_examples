# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: Maria
'''
#først bokstaver derefter tal

import tkinter as tk
import random
import string


def result():
    chara_set = string.ascii_uppercase
    char_set = string.ascii_lowercase
    num_set = string.digits
    resultVar.set((''.join(random.sample(chara_set,1)))+''.join(random.sample(char_set,6))+''.join(random.sample(num_set,3)))

mainWindow = tk.Tk()
mainWindow.title("Password Generator")
mainWindow.minsize(300, 100)
mainWindow.resizable(width=False, height=False)    

# Create a fraom to hold all the GUI elements

win = tk.Frame(mainWindow, width=300, height=100)
win.pack()

# StringVar is the connection from the GUI to the code in this file
# Update them with .set in the callback functions  
resultVar = tk.StringVar()
resultVar.set("")


win.pack()
button1 = tk.Button( win, text = "Generate", command = result).pack(side=tk.TOP)
textEntry1 = tk.Entry( win,  textvariable=resultVar).pack(side=tk.BOTTOM)

win.mainloop()
