import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

for i in range(len(people)):
    if (people[i] == "Waldo"):
        print("Waldo is Gevonden! Hij zat op plek:",i + 1)
        print(people)
