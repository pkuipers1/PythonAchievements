#Schrijf een functie die de letters van een woord willekeurig door elkaar schudt.
#Je mag deze code hiervoor hergebruiken.

#Bij het aanroepen van de functie moet je elk woord mee kunnen geven als argument.

#De functie moet het geschudde woord terug geven via een return.

#Roep de functie 3x aan met een ander woord en print de geschudde woorden uit.

import random

def randomiseLetters(original):
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)
    return original

randomiseLetters("test")
randomiseLetters("word")
randomiseLetters("Star")
