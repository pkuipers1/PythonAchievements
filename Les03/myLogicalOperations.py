name = "erwin henraat"
job = "teacher"
moneyInAccount = 1300

#Vervang de ** met de logische operatoren 'and' en/of 'or'

#Zorg dat de if statement de functie buyABrandNewMotorcycle uitvoert als:
# Mijn naam erwin henraat is en ik een baan heb.
# Of als ik meer dan 10000 euro op mijn rekening heb staan.
def buyABrandNewMotorcycle():
    for index in range(10):
        print("Je kan een motor kopen.")


if (name == "erwin henraat" and job != None) or moneyInAccount > 10000:
    buyABrandNewMotorcycle()
else:
    print("Je kan helaas geen motor kopen.")

if name != "erwin henraat" or moneyInAccount > 100000000:
    print("Hey, dit is óf Erwin Henraat óf een milionair!")
