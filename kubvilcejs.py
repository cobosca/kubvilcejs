import random
import time
import sys

print("KUBU VILKŠANAS TRENERIS AKTIVIZĒTS!")
time.sleep(1)
gatavs = input("\nGATAVS DARBAM? (y/n): ")
if gatavs != "y":
    sys.exit("MĪKSTAIS!")

beigt = False

while beigt != True:
    sakne = random.randint(1,101)
    manasakne = input(f"Kubsakne no {sakne*sakne*sakne} ir ...")
    if manasakne == str(sakne):
        print("Taisnība, vecozēn!")
        time.sleep(0.5)
        velvienu = input("Paņemsi vēlvienu? ")
        if velvienu == "y":
            continue
        else:
            sys.exit("Pārāk mīksts esi, ko?")
        
    else:
        pareizi = False
        while pareizi != True:
            print("Galīgi garām, vecais!")
            time.sleep(0.5)
            print("Dari atkal!")
            manasakne = input(f"Kubsakne no {sakne*sakne*sakne} ir ...")
            if manasakne == str(sakne):
                print("Taisnība, vecozēn!")
                pareizi = True
                break
                
                
            
            
        
        
        
