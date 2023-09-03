def presenteer (dictionary, totaal):
    for item, amount in dictionary.items():
        print(f"{item} : {amount} euro")
      
mijn_dict = {'vis' : 10, 'vlees': 25, 'overig': 15}
totaal = 50
presenteer (mijn_dict, totaal)

print("============================")
print(f"Totaal : {50} euro")    




