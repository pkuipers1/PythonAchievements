#Maak een Python bestand stel_vragen.py en schrijf de Python code die:

#Minstens drie vragen stelt en gebruik maakt van de input() functie
#Elk antwoord opslaat in een variabele
#Na het stellen van de vragen met de print() functie een goed lopende zin met alle antwoorden op het scherm zet.
#Let op: De variabele moet een duidelijke naam hebben zodat je weet wat er in wordt opgeslagen
#Vraag je bijvoorbeeld om een naam, een leeftijd en plaats dan zou er op het scherm kunnen staan:

#“Hey Hidde, je bent alweer 45 jaar en volgens mij woon je in Amsterdam, of niet?”

#gegevens opvragen en bewaren
naam = input('\nHello You! Wat is je naam?\n')
print('\n')
leeftijd = input('Oke, en wat is je leeftijd?\n')
print('\n')
woonplaats = input('En de laatste vraag, wat is je woonplaats?\n')

#gegevens teruggeven
print('\nHallo',naam,'! Jij bent dus',leeftijd,'jaar oud en woont in',woonplaats,'?\n')
