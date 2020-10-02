#ZELF EEN FUNCTIE MAKEN

def printHelloWorld():
    print("Hello World!")

printHelloWorld()

#Maak een functie, daarbinnen zet je print,
#Wat je daarbinnen wil doen is dat de waarde
#Die je meekrijgt geprint moet worden.

def printWaarde(waarde):
    print(waarde)

printWaarde(3)

def printWaardes(waarde1, waarde2 = True):
    print(waarde1, waarde2)

printWaardes(4)

def functieMetReturnValue():
    mijnVariabele = 0
    mijnVariabele += 1
    return mijnVariabele

resultaat = functieMetReturnValue()
print("resultaat is:", resultaat)
