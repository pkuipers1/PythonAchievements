#Je kunt stukjes uit een string variabele (een tekst) ophalen door in onderstaande deelopdrachten gebruik te maken van string ’slicing’.

#Bijvoorbeeld
#naam = "Luke Skywalker"
#voornaam = naam[0:4]
#print(voornaam)

# Luke
#Laat zien dat je string slicing beheerst door uit elke zin hier onder de juiste stukjes op te halen en op het scherm te zetten:


#Haal de voornamen uit deze tekst op en maak gebruik van string slicing
tekst1 = 'De Python lessen worden gegeven voor Erik, Erwin en ook door Hidde'
voornamen1 = tekst1[37:41]
voornamen2 = tekst1[43:48]
voornamen3 = tekst1[61:67]
print(voornamen1, voornamen2, voornamen3)

tekst2 = 'SD vakken zijn Python, UXD, Frontend development en Backend development en nog veel meer ...'
vak1 = tekst2[15:21]
vak2 = tekst2[23:26]
vak3 = tekst2[28:48]
vak4 = tekst2[52:71]
print(vak1, vak2, vak3, vak4)

tekst3 = 'Wat is hier het laatste woord?'
laatsteWoord = tekst3[-6:-1]
print(laatsteWoord)
                                                #29 = i!!!! im Be
tekst4 = 'Het www is ontwikkeld vanaf 1989 door Tim Berners-Lee'
L5_8 = tekst4[4:8]
L29_33 = tekst4[28:32]
print(L5_8, L29_33)
