#for loops allow the programmer to repeat

#write a program that prints the numbers 1 through 10
#range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0,10):   #0 is start value and 10 is stop value
    print(i)

top_foods = ["Eggs Benedict", "Fried Chicken", "Mac n Cheese"]
#Go through every food in top foods
#repeats everything contained in the for loop for every item in the list
#Food is the current item
for food in top_foods:
    print(food)


# create a list of groceries
# contains milk, eggs, bread, butter, apples
# ask for user input on an item they purchased
# if the item was on the list print("<item> crossed off")
# remove item

groceries = ["milk", "eggs", "bread", "butter", "apples"]
a = input("What item did you buy?\n> ")
a.lower()
if a in groceries:
    for item in groceries:
        if item == a:
            print(str(item)+" crossed off")
else:
    print(str(a)+" is not on the list")

#create a list of five random numbers 1-100
#find the sum of the numbers

import random

numbers = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),]
sum = 0
for i in numbers:
    sum += i
print(sum)