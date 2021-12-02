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

def keskmine(i,p):
    """
    :rtype var:
    """
    summa=0
    for palk in p:
        summma+=palk
    kesk=summa/len(p)
    print(kesk)
    vahe=0
    if 0<=p.index(kesk)<len(p)-1:
        kesk=i[p.index(kesk)]
        return kesk
    else:
        kesk="Peedub"
        return kesk

def suurim_palk(i:list, p:list):
    """Otsime suurim palk ja näitame kellel ta on
    :rtype float, str:
    """
    suurim=max(p)
    b=p.index(suurim)
    kellel=i[b]
    return suurim, kellel

def bs(pal, i):                                             #код не мой украл у Кристины.
    palgad=[]                                               #код не мой украл у Кристины.
    with open(pal) as f1:                                   #код не мой украл у Кристины.
        for stro in f1:                                     #код не мой украл у Кристины.
            palgad.append(stro.strip())                     #код не мой украл у Кристины.
    f=open(i, "r")                                          #код не мой украл у Кристины.
    inimesed=[]                                             #код не мой украл у Кристины.
    for stroka in f:                                        #код не мой украл у Кристины.
        inimesed.append(stroka.strip())                     #код не мой украл у Кристины.
    f.close()                                               #код не мой украл у Кристины.
    pal=palgad.copy()                                       #код не мой украл у Кристины.
    pal.sort()                                              #код не мой украл у Кристины.
    a=pal[0]                                                #код не мой украл у Кристины.
    b=palgad.index(a)                                       #код не мой украл у Кристины.
    return a, inimesed[b]                                   #код не мой украл у Кристины.

def lisa(nimi, palk):
    nimi=str(input("Nimi: "))
    inimised.append(nimi)
    palk=float(input("Palk: "))
    palgad.append(palk)
    return inimised,palgad

def lisamine(inimisedd, palgadd):
    kuipalju = int(input("Kui palju inimesi lisada: "))
    for j in range(kuipalju):
        nimi=input("Nimi: ")
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
