import random
best_elden_ring_weapons = ["Blasphemous blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's fang"]

#Index        0     1     2     3
best_years = [1776, 1985, 1994, 1957]
print(best_elden_ring_weapons[int(len(best_elden_ring_weapons))-1])

#Print worst best elden ring weapon
print(len(best_elden_ring_weapons))

#Strings are lists of characters
word = "List"
a = random.randint(0,3)
print(word[a])

#removes item at the position in the list
best_elden_ring_weapons.pop(4)

#remove item by value
#removes first occurrance of an item
best_elden_ring_weapons.remove("Moonveil")

#add new item to the end of the list
best_elden_ring_weapons.append("Mohgwyn's Sacred Spear")

numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),]
print(numbers)
numbers.sort()
print(numbers)

print(best_years.index(1985))