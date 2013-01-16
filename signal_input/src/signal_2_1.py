'''
Created on 15/01/2013

@author: jaaby_000
'''
myfile = open("c:/Datalog3.txt", encoding="utf-8")
myfile.readline()
numberoflines = sum(1 for line in myfile)

print(numberoflines)