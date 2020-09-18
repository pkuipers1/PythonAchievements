#Vertaal de onderstaande zin naar python code en gebruik daarbij het nesten van if en
#else statements en indien gewenst ook logische operatoren:

#Als ik honger heb en ik geen zin heb om te koken dan bestel ik pizza tenzij er
#nog een kliekje in de koelkast ligt. Dan eet ik die op. Als ik geen geld heb ga ik toch koken.

imHungry = True
wantToCook = True
kliekjeAanwezig = False
money = 40

if imHungry == True:
    if wantToCook == True:
        print("Je gaat koken.")
    elif kliekjeAanwezig == True:
        print("Je eet het kliekje.")
    elif money < 30:
        print("Je moet helaas toch koken.")
    else:
        print("Je kunt pizza bestellen!")
