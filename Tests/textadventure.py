import random
print("Welcome to <insert creative title>!")
print("\nWe start off in the fictional hellscape known by the name of New Jersey.")
print("Your only job is to escape.")

money = 16.50
ski_mask = False
apples = 0
savings_money = 8276.98
cargo_plane = False
def end_1():
    print("You fail to even wake up, and have no hope of leaving New Jersey.")  #New Jersey truly is an awful place
    print("ending 1")

def end_2():
    print("You forgot about the 9 bottles of lighter fluid you left in the oven, a rookie mistake.")
    print("Ending 2")

def end_3():
    print("You die of old age while the teller goes on and on about credit score and interest.")
    print("Ending 3")

def end_4():
    print("You fail to rob the bank, and get arrested.")
    print("Ending 4")

def end_5():
    print("You fail to escape.")
    print("Ending 5")

def end_6():
    print("The rats talk back and you become the Rat King.")
    print("Secret ending")

def end_7():
    print("You leave New Jersey, and enter New York.")      #I don't know how much better New York is
    print("True ending")

def end_8():
    print("You go home and take a nap.")
    print("ending 8")

def start():
    print("ACT 1\nYou awake to your alarm clock going off. do you:")
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
    print("1. Make breakfast (8 or higher)")
    print("2. Leave the kitchen without eating breakfast")

    choice = int(input("> "))
    if choice == 1:
        b = random.randint(1,20)
        print(b)
        if b >= 8:
            garage()
        else:
            end_2()
    elif choice == 2:
        print("You go to the garage without eating")
        garage()
    else:
        print("Invalid answer, try again")
        kitchen()

def garage():
    global choice1
    print("You are in the garage. Pick a vehicle.")
    print("1. 1987 Buick Grand National")
    print("2. 2017 Cadillac Escalde V")
    print("3. 1997 Toyoto Corolla")
    print("4. A mule you have hitched to the wall")

    choice1 = int(input("> "))
    if choice1 < 4:
        street()
    elif choice1 == 4:
        print("That wouldn't have been my choice, but you still continue")
        street()
    else:
        print("Invalid answer, try again")
        garage()

mule_steroids = False

def street():
    print("You can now make your way to one of three destinations:")
    print("1. The store (You have $"+str(money)+")" )
    print("2. The bank")
    print("3. The Lincoln Tunnel (The tunnel that leads out of New Jersey)")
    print("4. The Jets game")
    print("5. The Giants game")
    print("6. Some guy selling a cargo plane on Facebook Marketplace")
    print("7. Airport")

    choice = int(input("> "))
    if choice == 1:
        if choice1 == 4:
            print("It takes hours to get there due to the mule.")
        store()
    elif choice == 2:
        if choice1 == 4:
            print("It takes hours to get there due to the mule.")
        bank()
    elif choice == 3:
        chance1 = random.randint(1,10)
        if chance1 <= 5:
            mugged()
        else:
            gas_station()
    elif choice == 4:
        jets()
    elif choice == 5:
        giants()
    elif choice == 6:
        plane()
    elif choice == 7:
        airport()
    else:
        print("Invalid answer, try again")
        street()

def store():
    print("You are at the store. you can buy:")
    print("1. a ski mask ($5.00)")
    print("2. 6 dozen apples ($32.49)")
    print("3. Leave")
    if choice1 == 4:
        print("4. mule steroids ($0.78)")
    
    choice = int(input("> "))
    
    if choice == 1:
        if ski_mask == True:
            print("You already have one of these")
            store()
        elif money >= 5:
            global money
            global ski_mask
            print("You buy the ski mask.")
            money = money - 5.00
            ski_mask = True
            print("You now have $"+str(money))
            store()
        else:
            print("You don't have enough money")
        store()
        
    elif choice == 2:
        global apples
        global money
        if money >= 32.49:
            print("you buy 6 dozen apples")
            money = money-32.49
            apples += 72
            print("you are now at $"+str(money))
            store()
        else:
            print("you don't have enough money")
        store()
    elif choice == 3:
        street()
        
    elif choice == 4:
        global mule_steroids
        if money >= 0.78:
            print("Your mule is now much faster")
            money = money - 0.78
            print("you are now at $"+str(money))
            store()
        else:
            print("You don't have enough money")
            store()
    else:
        print("Invalid answer, try again")
        store()

def bank():
    print("you are at the bank you can:")
    print("1. take out a loan")
    print("2. rob the bank (5 or higher; +4 if you have a ski mask)")
    print("3. withdraw money ("+savings_money+"in account)")
    print("4. leave")

    choice = int(input("> "))

    if choice == 1:
        end_3()
    elif choice == 2:
        if ski_mask == True:
            a = random.randint(1,20)
            if a >= 9:
                c = random.randint(100,25000)
                print("successfully robbed the bank for $"+c+"!")
                street()
                money = money + c
            else:
                end_4()
        else:
            b = random.randint(1,20)
            if b >= 5:
                d = random.randint(100,25000)
                print("Successfully robbed the bank for $"+d+"!")
                money = money + d
                street()
            else:
                end_4()
    elif choice == 3:
        cash = int(input("How much money do you want to withdraw\n> "))
        if cash <= savings_money:
            money = money + cash
            savings_money = savings_money - cash
            print("Withdrew $"+cash)
            
        else:
            print("not enough money in account.")
        bank()
    elif choice == 4:
        street()
    else:
        print("Inavalid answer, try again")
        bank()

def mugged():
    print("When you stop at a gas station, you get cornered and one of them asks for all your money")
    print("1. give them all your money")
    print("2. attempt to escape (6 or higher)")

    choice = int(input("> "))

    if choice == 1:
        print("you give them all of your money")
        global money
        money = 0
        lincoln_tunnel()
    elif choice == 2:
        a = random.randint(1,20)
        if a >= 6:
            print("You successfully escape")
            lincoln_tunnel()
        else:
            end_5()
    else:
        print("Invalid answer, try again")
        mugged()

def gas_station():
    a = random.randint(1,10)
    if a >= 5:
        print("When you stop at a gas station, you are knocked unconscious, and wake up in a sewer surrounded by rats")
        print("1. Start talking to the rats")
        print("2. Leave the sewer and continue to the lincoln tunnel")

        choice = int(input("> "))

        if choice == 1:
            end_6()
        elif choice == 2:
            lincoln_tunnel()
    else:
        lincoln_tunnel()

def lincoln_tunnel():
    print("The final showdown; do you:")
    print("1. Leave New Jersey")
    print("2. Go home")

    choice = int(input("> "))

    if choice == 1:
        end_7()
    elif choice == 2:
        end_8()
    else:
        print("Invalid answer, try again")

def jets():
    print("you go to watch a Jets game, do you:")
    print("1. stay and watch them lose")
    print("2. leave")

    choice = int(input("> "))
    
    if choice == 1:
        print("They lose")
        street()
    elif choice == 2:
        street()
    else:
        print("invalid answer, try again")
        jets()

def giants():
    print("You go to a Giants game, do you:")
    print("1. watch them lose")
    print("2. leave")

    choice = int(input("> "))

    if choice == 1:
        print("They lose")
        street()
    elif choice == 2:
        street()
    else:
        print("Invalid answer, try again")
        giants()

def plane():
    print("You go see the guy selling the cargo plane")
    print("1. buy the plane for $1200")
    print("2. Leave")
start()