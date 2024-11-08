import random
num = random.randint(1,100)
ipnut = ''

while num != ipnut:
    try:
        ipnut = input("Guess the number\n> ")
        ipnut = int(ipnut)
        if ipnut > num:
            print("\nToo High!\n")
        elif ipnut < num:
            print("\nToo Low!\n")
    except:
        print("\nMake sure the answer is a number\n")
print("Correct")