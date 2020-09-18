#In een boomgaard staan 333 appelbomen.
#2/3 deel (indien noodzakelijk afgerond naar boven) van de bomen staat in de schaduw van een berg
#en geeft hierdoor maar 80% van de appels in vergelijking met de bomen die in de zon staan.
#Een boom die in de zon staat geeft precies 146 Appels.
#De boomgaard is van mij en 3 vrienden en we verdelen alle appels eerlijk.

#Bereken met behulp van een pythonscript hoeveel appels ik mag verkopen.
#In stukken gesneden appels zijn helaas niet te verkopen. Die eten we zelf op

#voor afronden
import math

#begin code
print('\nHello You! Dit is mijn Pythonscript om te berekenen hoe veel appels ik mag verkopen!\n')

#basisstatistieken
aantalBomenVanMij = 333 / 3 * 1
aantalBomenInSchaduw = aantalBomenVanMij / 3 * 2

aantalBomenInZon = aantalBomenVanMij - aantalBomenInSchaduw
appelenPBZon = 146
appelenPBSchaduw = 146 * 0.8

appelenPBSchaduwAfgerond = math.floor(appelenPBSchaduw)

appelenVanMij = appelenPBZon * aantalBomenInZon + appelenPBSchaduw * aantalBomenInSchaduw

appelenVanMijAfgerond = math.floor(appelenVanMij)

#basisinfo geprint
print('Aantal bomen van mij:',aantalBomenVanMij,'\n')

print('Aantal bomen van mij die in de zon staan:',aantalBomenInZon)
print('Aantal bomen van mij die in de schaduw staan:',aantalBomenInSchaduw,'\n')

print('Appelen per boom die in de zon staat:',appelenPBZon)
print('Appelen per boom die in de schaduw staat:',appelenPBSchaduwAfgerond,'\n')

print('Mijn totaal aantal appelen:',appelenVanMijAfgerond,'\n')
