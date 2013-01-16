'''
Created on 15/01/2013

@author: jaaby_000
'''
myfile = open("c:/Datalog2.txt","r", encoding="utf-8")
myfile.readline()
maxder = ["0"]
minder = ["0"] 
def minlykke():   
     
    for line in myfile.readlines():     
        vac = line.strip()
        vac3 = vac.split('\t')
        vac4 = vac3[1]
        print(vac4)
        if float(vac4) > float(maxder[0]):
            maxder.pop(0)
            maxder.append(vac4)
        if float(vac4) < float(minder[0]):
            minder.pop(0)
            minder.append(vac4)
      
minlykke()
print("Max. Value\t" + maxder[0])
print("Min. Value\t" + minder[0])