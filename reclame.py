def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = 1 * (4 - 0.4)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

aanbieding = aanbieding_1("aardbei", 4, 0.40)
print(aanbieding)

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    inkomsten = [220,430,125,160,205,90,345]
    btw_bedrag = 0.09
    for bedrag in inkomsten:
        totaal = totaal + bedrag
        btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return totaal, uitvoer

inkomsten = [220,430,125,160,205,90,345]
btw_bedrag = 0.09
resultaat = inkomsten_totaal([220,430,125,160,205,90,345],0.09)
print(resultaat)

def laag_en_hoog(mijn_lijst):
    mijn_lijst = [220,430,125,160,205,90,345]
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer

mijn_lijst = [220,430,125,160,205,90,345]
resultaat = laag_en_hoog(mijn_lijst)
print(resultaat)

def gemiddelde(mijn_lijst):
    mijn_lijst = [220,430,125,160,205,90,345]
    aantal = len(mijn_lijst)   
    totaal = 0
    for element in mijn_lijst:
        totaal = totaal + element
        gemiddelde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    
uitvoer = gemiddelde(mijn_lijst)
print(uitvoer)

def meervoudig(invoer_lijst):
    invoer_lijst = [10,5,3,2,1,2,9]
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0],tijdelijk[1]]
    return uitvoer

invoer_lijst = [10,5,3,2,1,2,9]
resultaat = meervoudig(invoer_lijst)
print(resultaat)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    laagste = min(korte_lijst)   
    hoogste = max(korte_lijst) 
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
def mijn_functie_2(a,b):
    return a + b

korte_lijst = [10,5,3,2,1,2,9]
resultaat = combinatie(invoer_lijst_2=laag_en_hoog)
print(resultaat)
   





    









    
    
    







    


























    








 

    
    
   





    









    
    
    







    


























    




>>>>>>> 13d4edf963ee4a234d7d272a52dc1c7800d7f8c3
