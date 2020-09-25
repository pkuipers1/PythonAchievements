print("Hello World! Welkom bij mijn daily choices programma.\n\n")

question1 = "Je wekker gaat. Wat doe je?\n\nA. Snooze\nB. Meteen opstaan\n"
question2 = "Je hebt keuze tussen brood, muesli of géén ontbijt. Wat doe je?\n\nA. Ik neem brood.\nB. Ik neem muesli.\nC. Ik neem liever niks.\n"
question3 = "Je gaat van het station naar het Mediacollege. Ga je lopend of met de bus?\nA. Lopend\nB. Met de bus\n"
question4 = "Je hebt huiswerk op gekregen van Python en BWP. Welke ga je doen?\nA. Python\nB. BWP\n"
question5 = "Je hebt vrij. Waar ga je je tijd aan besteden?\nA. Werken aan je boot.\nB. ARK: Survival Evolved Spelen.\n"


print(question1)

def choice1loop():
    answerOf1 = input()
    if answerOf1 == "a" or answerOf1 == "A":
        print("Je Snoozed de wekker.\n\n")
        print(question2)
    elif answerOf1 == "b" or answerOf1 == "B":
        print("Je staat meteen op.\n\n")
        print(question2)
    else:
        print("Ongeldige invoer.\n\n")
        choice1loop()
choice1loop()

def choice2loop():
    answerOf2 = input()
    if answerOf2 == "a" or answerOf2 == "A":
        print("Je kiest voor brood.")
        print(question3)
    elif answerOf2 == "b" or answerOf2 == "B":
        print("Je neemt muesli.")
        print(question3)
    elif answerOf2 == "c" or answerOf2 == "C":
        print("Je eet geen ontbijt. Dat is niet zo gezond hoor!")
        print(question3)
    else:
        print("Ongeldige invoer.\n\n")
        choice2loop()
choice2loop()

def choice3loop():
    answerOf3 = input()
    if (answerOf3 == "a" or answerOf3 == "A"):
        print("Je gaat lopend naar het MA.")
        print(question4)
    elif (answerOf3 == "b" or answerOf3 == "B"):
        print("Je gaat met de bus naar het MA.")
        print(question4)
    else:
        print("Ongeldige invoer.\n\n")
        choice3loop()
choice3loop()

def choice4loop():
    answerOf4 = input()
    if (answerOf4 == "a" or answerOf4 == "A"):
        print("Goeie keuze!")
        print(question5)
    elif (answerOf4 == "b" or answerOf4 == "B"):
        print("Veel Success!")
        print(question5)
    else:
        print("Ongeldige invoer.\n\n")
        choice4loop()
choice4loop()

def choice5loop():
    answerOf5 = input()
    if (answerOf5 == "a" or answerOf5 == "A"):
        print("Je gaat aan je boot werken. Die kan nog een flinke opknapbeurt gebruiken.")
    elif (answerOf5 == "b" or answerOf5 == "B"):
        print("ARK, de oude favoriet!")
    else:
        print("Ongeldige invoer.\n\n")
        choice5loop()
choice5loop()
