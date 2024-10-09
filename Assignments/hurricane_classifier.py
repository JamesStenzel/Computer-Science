speed = int(input("What is the wind speed in MPH?\n>"))

if speed < 74:
    print("This is classified as a tropical storm")

elif speed < 96:
    print("This is classified as a Category 1 hurricane")

elif speed < 111:
    print("This is classified as a Category 2 hurricane")

elif speed < 130:
    print("This is classified as a Category 3 hurricane")

elif speed < 157:
    print("This is classified as a Category 4 hurricane")

else:
    print("This is classified as a Category 5 hurricane")