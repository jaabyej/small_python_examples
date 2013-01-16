'''
Created on 09/01/2013

@author: jaaby_000
'''
import random
import math
def minlykke():
    nummer = 0
    sine = 0
    newsine = 0
    tilf = 0
    samlet = 0
    myfile = open("c:/Datalog5.txt", "w")
    myfile.write("Time/ms\tInput1\tInput2\tSamlet\n")
    for x in range (1,51):    
           
        for x in range (1,21):
            tilf = random.uniform(-1, 1)
            samlet = sine + tilf
            myfile.write(str(nummer) + "\t" + str("%.3f" % sine) + "\t" + str("%.3f" % tilf) + "\t" + str("%.3f" % samlet) + "\n")
            nummer += 1
            newsine += 1
            sines = 2 * math.pi * newsine / 20
            sine = math.sin(sines)      
    myfile.close()   
minlykke()