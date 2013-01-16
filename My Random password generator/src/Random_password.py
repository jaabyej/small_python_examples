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
    resultVar.set((''.join(random.sample(chara_set,1)))+''.join(random.sample(char_set,1))+''.join(random.sample(num_set,6)))

mainWindow = tk.Tk()
mainWindow.title("Password Generator")
mainWindow.minsize(350, 250)
mainWindow.resizable(width=False, height=False)    

mainWindow.rowconfigure('all', option = 200)
mainWindow.columnconfigure('all', option = 200)
mainWindow.rowconfigure('all', weight = 3)
mainWindow.columnconfigure('all', weight = 3)
# Create a fraom to hold all the GUI elements

win = tk.Frame(mainWindow, borderwidth=125, bg = 'darkgreen', width=350, height=250)
win.pack()

# StringVar is the connection from the GUI to the code in this file
# Update them with .set in the callback functions  
resultVar = tk.StringVar()
resultVar.set("")


win.pack()
button1 = tk.Button( win, text = "Generate", command = result)
button1.grid(row=4, column=3 )
textEntry1 = tk.Entry( win,  textvariable=resultVar)
textEntry1.grid(row=2, column=3 )
win.mainloop()
