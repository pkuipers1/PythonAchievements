#Maak een script met een aantal berekeningen waarbij je de volgende operatoren gebruikt:

#toekennen (assignment) =
#optellen +
#aftrekken -
#delen /
#restwaarde (modulo) %
#optellen bij waarde van variabele +=
#delen door waarde van variabele /=
#Welke rekenkundige operatoren missen er in dit lijstje? Bedenk welke dit zijn en gebruik deze ook in je code.

#variabelen
numA = 10
numB = 10
numC = 10
numD = 30

#weergeven
print('\nHello You! Dit is mijn Pythonopdracht over Operators!\n')
print('numA =',numA)
print('numB =',numB)
print('numC =',numC,'\n')

#berekeningen
numABC = numA * numB * numC
numAplusB = numA + numB
numAminB = numA - numB
numAdelendoornumB = numA / numB

#maak numC 50
numC = 50

#meer berekeningen
numB += numC
numA /= numB

#numE modulo berekening en macht
numE = 15
numE = numD % numA
numF = numA ** numB

#opnieuw weergeven
print('numABC =',numABC)
print('numAplusB =',numAplusB)
print('numAminB =',numAminB)
print('numAdelendoornumB =',numAdelendoornumB,'\n')

print('numA is bewerkt, numA =',numA)
print('numB is bewerkt, numB =',numB)
print('numC is bewerkt, numC =',numC,'\n')

print('numE = numD modulo numA, numE =',numE)
print('numA tot de macht numB =',numF,'\n')
