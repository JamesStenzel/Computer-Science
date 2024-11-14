# break
#exits loop prematurely
import random
bag_of_fruit = ["apple", "orange", "bug", "watermelon", "pear"]
random.shuffle(bag_of_fruit)
for x in bag_of_fruit:
    if x == "bug":
        print("You found a bug in the bag")
        break
    else:
        print("You ate a "+x)

#continue
#skips current loop
#it doesn't exit the entire loop, just moves on to the next iteration
orders = [15, 30, 35, 23, 100, 3, 10, 22]

#only apply discount for orders above $20
for order in orders:
    if order > 20:
        print("$"+str(order)+" discounted to $"+str(order * 0.95))
    else:
        continue

#pass
#does nothing
#usually used as a placeholder

def enter_forest():
    pass
