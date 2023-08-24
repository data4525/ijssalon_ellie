def som (inkomsten):
    total = sum(inkomsten.values())
    return total

inkomsten = {
    'Aardbeien-ijs-totaal': 1000,
    'Vanille-ijs-totaal': 2000,
    'Chocolade-ijs-totaal': 1500,
    'Waterijsjes-totaal': 750,

}

resultaat = som(inkomsten)
print(resultaat)

