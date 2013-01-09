'''
Created on 08/01/2013

@author: jaaby_000
'''

def minlykke():
    nummer = 0
    myfile = open("c:/Datalog1.txt", "w")
    myfile.write("Time/ms\tInput/Volts\n")
    for x in range (1,1002):
        
        myfile.write(str(nummer) + "\t0\n")
        nummer += 1
    
    myfile.close()
    
minlykke()