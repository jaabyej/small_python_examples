'''
Created on 08/01/2013

@author: jaaby_000
'''
import random

def minlykke():
    nummer = 0
    tilf = 0
    myfile = open("c:/Datalog2.txt", "w")
    myfile.write("Time/ms\tInput/Volts\n")
    for x in range (1,1002):
        tilf = random.uniform(-1, 1)
        myfile.write(str(nummer) + "\t" + str("%.3f" % tilf) + "\n")
        nummer += 1
    myfile.close()    
minlykke()