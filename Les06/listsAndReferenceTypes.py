lijstje = ["appeltje1","appeltje2","appeltje3"]
# INDEX:       0           1            2

# HET IS BETER ALS EEN LIJSTJE ITEMS VAN HETZELFDE
# TYPE BEVAT. BIJV. ALLEMAAL GETALLEN, STRINGS, ETC.

# In Python mag je verschillende datatypes van items
# In een lijstje zetten.

lijstje.append("appeltje4")
# Van dit opject wil ik ... Deze functie
# uitvoeren/variabele hebben
# Dit voegt appeltje4 toe aan de lijst.

lijstje.insert(0, "appeltje0")
# Voegt appeltje0 toe op plek 0 van de lijst

lijstje.remove("appeltje4")
# Verwijdert het eerste item van die waarde

aantalAppeltje1 = lijstje.count("appeltje1")
# Geeft het aantal keer terug dat appeltje1 in
# De lijst staat.

print("Aantal Appeltje1's:",aantalAppeltje1)

print(lijstje)



# LISTWAARDE OPHALEN EN ZETTEN:
waardeA = lijstje[0]
lijstje[0] += "abc"

print(lijstje)

# Reeks van waardes opvragen
lijstA = lijstje[0:2]
# Index 0 tot 2
lijstB = lijstje[:1]
# Index 0 tot 1
lijstC = lijstje[1:]
# Index 1 tot einde

print(lijstA)
print(lijstB)
print(lijstC)
