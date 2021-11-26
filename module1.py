from random import *

def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    f=open(file,"r")
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_

def lisamine(inimisedd, palgadd):
    kuipalju = int(input("Kui palju inimesi lisada: "))
    for j in range(kuipalju):
        nimi=str(input("Nimi: "))
        inimisedd.append(nimi)
        palk=float(input("Palk: "))
        palgadd.append(palk)
        return inimisedd,palgadd

def otsing_nimi_jargi(inimesed:list,palgad:list):
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene.upper()==nimi.upper():
            n=inimesed.count(nimi)
            print("Inimene on olemas, selline nimi kohtume",n, "korda")
            b=0
            t=[]
            for i in range(n):
                k=inimesed.index(nimi,b)
                palk=palgad[k]
                b+=k+1
                t.append(nimi+str(palk))
                #print(nimi, palk)
        else:
            t="Ei ole nimi kirjas"
    return t

def tulumaks():
    palk=str(input("Sisesta plak:" ))
