x = 0

if x > 0:
    print("x is a positive number")

elif x < 0:
    print("x is a negitive number")

else:
    print("x is 0")


color = input("What color is the light?\n>")

if color.lower() == "green":
    print("go")

elif color.lower() == "red":
    print("stop")

elif color.lower() == "yellow":
    print("come to a stop if you can do so safely")

else:
    print("call the police")