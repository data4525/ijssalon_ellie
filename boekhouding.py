import helper
import csv
from helper import som
from presentatie import presenteer

inkomsten = {
    'Aardbeien-ijs-totaal': 1000,
    'Vanille-ijs-totaal': 2000,
    'Chocolade-ijs-totaal': 1500,
    'Waterijsjes-totaal': 750
}

totaal_inkomsten = som(inkomsten)
presenteer (inkomsten, totaal_inkomsten)

print("============================")
print (f"Totaal: {totaal_inkomsten} euro")

with open ('boekhouding.csv','w',newline='') as csvfile:
                for key, value in inkomsten.items():
                            writer = csv.writer(csvfile,delimiter=';')
                            writer.writerow ([key,value])


