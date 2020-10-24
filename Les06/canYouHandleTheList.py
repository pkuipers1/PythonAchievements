#Maak een List aan en zet daar in minimaal 5 items met minimaal 3 verschillende datatypes.

#Voer op correcte wijze naar keuze 3 verschillende List Methods uit en print daarna steeds de inhoud van je List.
#Print indien van toepassing ook het resultaat van de method. (Bij een return)

lijstje1 = ["appel", 1, "hond", 3.5, False]

print("De lijst is nu:", lijstje1)

lijstje1.append("appel")

print("Met nog een appel is de lijst:", lijstje1)

aantalAppeltjes = lijstje1.count("appeltje")

print("Het aantal appels in de lijst is nu:", aantalAppeltjes)

lijstje1.reverse()

print("De lijst omgedraait is:", lijstje1)
