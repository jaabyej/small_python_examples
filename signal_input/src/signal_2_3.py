'''
Created on 16/01/2013

@author: jaaby_000
'''
myfile = open("c:/Datalog4.txt","r", encoding="utf-8")
myfile.readline()

 
def minlykke():   
    teller = 0 
    cunt = 0
    line = myfile.readline()
    vac = line.strip()
    vac3 = vac.split('\t')
    vac4 = vac3[1]
    if str(vac4) == "0.000":
            cunt += 1
            teller += 1
            for line in myfile.readlines(): 
                
                vac = line.strip()
                vac3 = vac.split('\t')
                vac4 = vac3[1]
                
                if str(vac4) == "0.000":
                    teller += 1
            
                if str(vac4) == "-0.000":
                    teller += 1
                cunt += 1
    if str(vac4) == "-0.000":
            cunt += 1
            teller += 1
            for line in myfile.readlines(): 
                
                vac = line.strip()
                vac3 = vac.split('\t')
                vac4 = vac3[1]
                
                if str(vac4) == "0.000":
                    teller += 1
            
                if str(vac4) == "-0.000":
                    teller += 1
                cunt += 1
    teller = teller / cunt * 500
    
    
    print(str(teller) + "Hz")    
minlykke()

