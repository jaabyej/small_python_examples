'''
Created on 20/12/2012

@author: jaaby_000
'''
import tkinter as tk

from threading import Timer

def timercallback():
    textVar.set("Insert Coins")
    
def result1():
    resultVar.set( str(int(resultVar.get())+1) )
      
def result2():
    resultVar.set( str(int(resultVar.get())+2) )
  
def result5():
    resultVar.set( str(int(resultVar.get())+5) )
    
def result10():
    resultVar.set( str(int(resultVar.get())+10) )
    
def result20():
    resultVar.set( str(int(resultVar.get())+20) )

def resultcancel():
    resultVar.set( str( 0) )
    textVar.set("Returning Coins")
    mytimer = Timer(2, timercallback)
    mytimer.start()
        
def resultcoke():
    
    if int(resultVar.get()) >= 12 :
        resultVar.set( str(int(resultVar.get())-12) )
        textVar.set("Dispencing")
        mytimer = Timer(2, timercallback)
        mytimer.start()
                
    elif int(resultVar.get()) < 12 :
        textVar.set("Not Enough Coins")
        mytimer = Timer(2, timercallback)
        mytimer.start()

def resultfanta():    
    if int(resultVar.get()) >= 10 :
        resultVar.set( str(int(resultVar.get())-10) )
        textVar.set("Dispencing")
        mytimer = Timer(2, timercallback)
        mytimer.start()
    
    elif int(resultVar.get()) < 10 :
        textVar.set("Not Enough Coins")
        mytimer = Timer(2, timercallback)
        mytimer.start()
        
mainWindow = tk.Tk()
mainWindow.title("Vending Machine")

win = tk.Frame()

resultVar = tk.StringVar()
resultVar.set("0")

textVar = tk.StringVar()
textVar.set("Insert Coins")

win.pack()
label1 = tk.Label( win, textvariable=textVar).pack(side=tk.TOP)
textEntry1 = tk.Entry( win,  textvariable=resultVar).pack(side=tk.TOP)
button1 = tk.Button( win, text = "1 kr.", command = result1, cursor="plus").pack(side=tk.TOP)
button2 = tk.Button( win, text = "2 kr.", command = result2, cursor="plus").pack(side=tk.TOP)
button5 = tk.Button( win, text = "5 kr.", command = result5, cursor="plus").pack(side=tk.TOP)
button10 = tk.Button( win, text = "10 kr.", command = result10, cursor="plus").pack(side=tk.TOP)
button20 = tk.Button( win, text = "20 kr.", command = result20, cursor="plus").pack(side=tk.TOP)
buttoncancel = tk.Button( win, text = "Cancel", command = resultcancel, cursor="pirate").pack(side=tk.TOP)
buttoncoke = tk.Button( win, text = "Coke", command = resultcoke).pack(side=tk.LEFT)
buttonfanta = tk.Button( win, text = "Fanta", command = resultfanta).pack(side=tk.RIGHT)

win.mainloop()