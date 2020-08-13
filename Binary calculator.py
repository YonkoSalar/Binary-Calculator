
valg = int(input("Trykk [1] for decimaltall->binary eller [2] for binary -> decimaltall \n"))

def binaryUt ():
    binary = []
    decimaltall = float(input("Tast inn et decimaltall: "))
    while True:
        if(decimaltall % 2 == 0):
            binary.append(0)    
        else:
            binary.append(1)
            
        if(decimaltall == 0.0):
            binary.reverse()
            return binary
        decimaltall = decimaltall // 2


def decimalUt():
    binaryNr = str(input("Tast inn binært tall: "))
    tot = 0
    liste = [int(i) for i in str(binaryNr)]
    liste.reverse()
    for i in range(len(liste)):
        tot += 2**(i*liste[i])
    print(tot)
        
        
    

if(valg == 1):
    skrivUtBin = binaryUt()
    print("Binary: " + str(skrivUtBin))

elif(valg == 2):
    skrivDeci = decimalUt()





    
