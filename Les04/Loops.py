import random

isRunning = True

while (isRunning == True):
    print("herhaal!")
    if ( random.randrange(0, 2) == 1 ):
        isRunning = False
else:
    print("Doe als laatste dit")


print("Einde programma")

lijstA = ["tekst", 1, True, 44.05]
lijstB = ["dit","is","een","reeks","tekst"]

print(lijstA)
print(lijstA[2])

print(lijstB)
lijstB[1] = "VERANDERD!"
print(lijstB)

#D00r lijst b heen gaan:
for waarde in lijstB:
    print("Dit is waarde:", waarde)

lijstGrootte = len(lijstA)
print("lijstA is", lijstGrootte, "lang.")

for waarde in lijstB:
    waarde = "iets"
    print(waarde)

print(lijstB)

for waarde in range( len ( lijstB ) ):
    if (lijstB[waarde] == "reeks"):
        lijstB[waarde] = "REEKS IS VERANDERD!"
    print(lijstB[waarde])

print(lijstB)



objects = [ "Viool", "Bal", "Beker", "Tafel" ]

print(objects)



for index in range( len( objects ) ) : # Zoek en verwijder de bal

    print(index)
    if ( objects[ index ] == "Bal" ) : # Gevonden! Stop met zoeken…
        objects[ index ] = ""
        break

print("Bal verwijderd! (Leeg gemaakt.)")
print(objects)



#makkelijk controleren of een waarde in jouw lijst staat

if "Beker" in objects:
    print("JA, ER ZIT EEN BEKER IN MIJN LIJSTJE!")

print("Welke waarde zoeken?")
gewensteWaarde = input()

if gewensteWaarde in objects:
    print("Ja,",gewensteWaarde,"zit erin.")
else:
    print("Nee,",gewensteWaarde,"zit niet in de lijst.")
