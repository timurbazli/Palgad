from module1 import * 
palgad=loe_failist_listisse("Palgad.txt")
inimesed=loe_failist_listisse("Inimesed.txt")

while True:
    print("0-Välja\n1-Lisamine\n2-Kõik\n3-Otsing nimi jargi")
    v=int(input())
    if v==0:
        break
    elif v==1:
        inimesed,palgad=lisamine(inimesed, palgad)
        print("\n")
    elif v==2:
        i=0
        for inimesed in inimesed:
            print(inimesed, end="-")
            print(palgad[i])
            i+=1
            print("\n")
    elif v==3:
        vastus=otsing_nimi_jargi(inimesed, palgad)
        print(vastus)
        print("\n")
    elif v==4:
        print("\n")