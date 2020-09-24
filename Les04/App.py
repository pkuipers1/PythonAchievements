import os
isRunning = True
antwoord = ""

positieX = 0

while (isRunning):

    #Vraag om input:
    print("Wat wil je doen?")
    antwoord = input()

    if (antwoord == "quit" or antwoord == "Quit"):
        isRunning = False
        break

    #Game Updaten:
    if (antwoord == "rechts"):
        positieX += 1
    elif (antwoord == "links"):
        positieX -= 1


    #Game Tekenen:

    #Scherm eerst schoonmaken, dan pas tekenen
    os.system("cls")

    for pos in range(positieX):
        print(" ", end="")
    else:
        print("0")
    print("-----------------------------")
