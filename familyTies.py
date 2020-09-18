#Schrijf een Python script waarin je gegevens over jezelf (en je familie?) eerst in een aantal
#variabelen opslaat en daarna op het scherm print en mixt met gewone tekst.

#Door het print() statement te gebruiken en een concatenation operator (een komma of een plus)
#zet je de inhoud van de variabelen als een goed lopende zin op het scherm.

#Kies voor elk gegeven het juiste data type: string, int of float en verzin zelf duidelijke namen voor de variabelen:

#Je naam
#Je leeftijd
#Je woonplaats
#Afstand tot school in kilometers, met tenminste 1 cijfer achter de komma
#... andere leuke informatie over jezelf
#Uiteindelijk zet je alle gegevens met de print() functie op het scherm.

#De output van het Python script is dan bijvoorbeeld:

#Mijn naam is Hidde, ik ben 45 jaar oud en woon in Amsterdam.
#Ik woon 4.3 kilometer van het Mediacollege.

#gegevens opvragen - staat in een functie
def gegevensOpvragen():

    print('\nHello You! Dit is mijn programma genaamd familyTies!')

    naam = input('Naam:\n') #string
    leeftijd = input('Leeftijd:\n') #int
    woonplaats = input('Woonplaats:\n') #string
    afstandTotSchool = input('Afstand tot school in KM met tenminste één cijfer achter de komma:\n') #float
    favorieteEten = input('Favoriete eten:\n')

    print('Hallo,',naam,', jij bent dus',leeftijd,'jaar oud en woont in',woonplaats,',',afstandTotSchool,'KM ver van school. Je favoriete eten is',favorieteEten,'!\n')

    opnieuw = input('Wil je het programma herstarten? Type ja of nee.\n')
    if opnieuw == "ja":
        gegevensOpvragen()
    else:
        print('Doei!\n')

gegevensOpvragen()
