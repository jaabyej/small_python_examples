'''
Created on 09/01/2013

@author: jaaby_000
'''
import math
def minlykke():
    nummer = 0
    sine = 0
    newsine = 0
    myfile = open("c:/Datalog4.txt", "w")
    myfile.write("Time/ms\tInput/Volts\n")
    for x in range (1,51):       
        for x in range (1,21):
            myfile.write(str(nummer) + "\t" + str("%.3f" % sine) + "\n")
            nummer += 1
            newsine += 1
            sines = 2 * math.pi * newsine / 20
            sine = math.sin(sines)      
    myfile.close()   
minlykke()
