#write a program tht asks for two numbers, and adds them
def divide_two():
    try:
        x = int(input("first number\n>"))
        y = int(input("second number\n>"))
    
        print(x / y)
    
    except ValueError:
        print("Enter a Number")
        divide_two()
    except ZeroDivisionError:
        print("can't divide by 0")
        divide_two()
    
    finally:
        print("\nDone\n_____\n___\n_____")
divide_two()