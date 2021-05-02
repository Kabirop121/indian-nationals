print("-------------WELCOME TO INDIA NATIONALS PROJECT---------------")

value = input("Enter keyworld eg: bird: ")
value2 = value.upper()
value3 = "NATIONAL" + " " + value2
dict1 = {
    "NATIONAL FRUIT" : 'Mango is national fruit of india',
    "NATIONAL ANIMAL" : 'Tiger is national animal of india',
    "NATIONAL BIRD" : "Peacock is national bird of india",
    "NATIONAL SONG" : "Vande matram is national song of india",
    "NATIONAL CURRENCY" : "Indian rupee is national currency of india",
    "NATIONAL PLEDGE" : '''India is my country and all \nIndians are my brothers and sisters. \nI love my country and \nI am proud of its rich and varied heritage. \nI shall always strive to be worthy of it.\n I shall give respect to my parents, \nteachers and elders and treat everyone with courtesy.''',
    "NATIONAL CALENDAR" : 'SAKA CALENDAR',
    "NATIONAL RIVER" : 'GANGA',
    "NATIONAL FLOWER" : 'LOTUS',
    "NATIONAL TREE" : 'INDIAN BANYAN',
    "NATIONAL AQUATIC ANIMAL" : "GANGA' RIVER DOLPHIN",
    "NATIONAL REPTILE" : 'KING COBRA',
    "NATIONAL HERITAGE ANIMAL" : 'INDIA ELEPHANT',
    "NATIONAL GAME" : 'HOCKEY'

}


for x in dict1:
    if x != value3:
        continue
    if x == value3:
         break
    else:
        print("No keyword found")

print(dict1[x])

# DOWLOAD NATIONALINDX.TXT AND READ IT FOR HELP
