firstFood = "Pizza"
secondFood = "Grilled Cheese"
thirdFood = "Macaroni and Cheese"
fourthFood = "Dumplings"
fifthFood = "Ice cream"

favFoods = ["Pizza", "Grilled Cheese", "Macaroni and Cheese", "Dumplings", "Ice cream"]

#What could you do to the list?
# - Search the list
# - Categorize
# - Add to it
# - Move items around 
# - Get the length of the list
# - Change an item
# - Remove items

## CRUD - Create, Read, Update, Delete

## To create an empyty list:
emptyList = []

## To read a list

print(favFoods[0])
print(favFoods[4])

## To update an item in the list

print (favFoods[2])
favFoods[2] = "Cake"
print (favFoods[2])

## Update list to inclde another item

favFoods.append("Italian Ice")
print(favFoods)

#Print using our list

for food in favFoods:
    print ("I sure do love " + food + "!")


#Dictionary

dstamp1 = ["Derek", "Stampone", 30, "Brown", "Brown", 5.7, 185, 8, True]
dstamp1_firstname = dstamp1[0]

dstamp1 = {"firstname": "Derek",
    "lastname": "Stampone",
    "age": 30,
    "eyecolor": "Brown",
    "haircolor": "Brown",
    "height": 5.8,
    "weight": 185,
    "lucky_number": 8,
    "registed_to_vote?": True
}

print(dstamp1["lucky_number"])

dstamp1["lucky_number"] = 7

dstamp1["ethnicity"] = "White" #Add key and value, adding and updating is same format

print(dstamp1)

superheroes = {
 "jeff": "Rogue",
 "deanna": "Jessica Jones",
 "danny": "Static Shock",
 "ash": "Supergirl",
 "derek": "The Hulk",
}

superheroes["Sophia"] = "All Might"

print(superheroes)

for person in superheroes:
    print(person + "'s favorite superhero is " + superheroes[person])
    


#Range

##Print every number from 1-100
for x in range(1, 101):
    print(x)
    
##Print ever even number from 1-100
for x in range (1, 101):
    if x%2 ==0:
        print(x)

#or

for x in range(2, 101, 2):
    print(x)
    
#or

for x in range(1, 51):
    print(x*2)
##Print out all the square numbers that are less than a million

for x in range(1, 1000001):
    if x**2 < 1000000:
        print (x**2)

#Nested
#This is a list of dictionaries
actors  = [
  {"name": "Molly Ringwald", "role": "Claire Standish", "grade": 10},
  {"name": "Judd Nelson", "role": "John Bender", "grade": 12},
  {"name": "Ally Sheedy", "role": "Allison Reynolds", "grade": 11},
  {"name": "Anthony Michael Hall", "role": "Brian Johnson", "grade": 10}
]

print(actors[2]["name"])

#What would I use to access the string "Brian Johnson"?

print(actors[3]["role"])

#What would I write if I wanted to count how many actors there are in this movie?

print(len(actors))

#Print out "The role of ___ was played by ___"

for person in actors:
    print ("The role of " + person["role"] + " was played by " + person["name"])

#or

for actor in actors:
    print("The role of %s was played by %s" %(actor["role"], actor["name"]))
