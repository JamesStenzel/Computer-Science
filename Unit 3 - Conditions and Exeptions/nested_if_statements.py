#Nested if statements

prime = True
cost = 20
age = 17
consent = False

if prime == True:
    if age >= 18:
        print("You are eligible for free shipping.")
    else:
        if consent == True:
            print("You are eligible for free shipping.")
        else:
            print("You are not eligible for free shipping.")
elif cost >= 25:
    if age >= 18:
        print("You are eligible for free shipping.")
    elif consent == True:
        print("You are eligible for free shipping.")
    else:
        print("You are not eligible for free shipping.")
else:
    print("You are not eligible for free shipping.")



# Do we need an umbrella

# We need an umbrella if it is e=raining and outside
raining = True
outside = True

if raining and outside:
    print("bring an umbrella")
else:
    print("umbrella not needed")

if raining:
    if outside:
        print("bring an umbrella")
    else:
        print("umbrella not needed")
else:
    print("umbrella not needed")
    