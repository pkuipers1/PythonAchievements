def Convert(string):
	li = list(string.split(" "))
	return li

print("Geef een zin op om te converteren en druk op enter:")
str1 = input()

list = Convert(str1)

for i in (list):
    if len(i) > 3:
        list[list.index(i)] = "abc"

print(list)
