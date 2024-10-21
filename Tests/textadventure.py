import random
print("Welcome to <insert creative title>!")
print("\nWe start off in the fictional hellscape known by the name of New Jersey.")
print("Your only job is to escape.")

def end_1():
    print("You fail to even wake up, and have no hope of leaving New Jersey.")  #New Jersey truly is an awful place
    print("ending 1 of 20")

def start():
    print("You awake to your alarm clock going off. do you:")
    print("1. try to get out of bed (10 or higher)")
    print("2. hit snooze and go back to sleep")

    choice = int(input("> "))
    if choice == 1:
        a = random.randint(1,20)        #Rolls d20
        print(a)
        if a >= 10:                     #Checks if over 10
            kitchen()
        else:
            end_1()
    elif choice == 2:
        end_1()
    else:
        print("Invalid answer, try again")
        start()

def kitchen():
    print("After successfully getting out of bed, you go to the kitchen. do you:")
    print("1. Make breakfast")
    print("2. Leave the kitchen without eating breakfast")
    print("3. ")

start()