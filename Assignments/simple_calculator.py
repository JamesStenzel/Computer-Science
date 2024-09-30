def add():
    print("Add two numbers:")
    x = int(input("1st number\n>"))
    y = int(input("2nd number\n>"))
    print(str(x), "+", str(y), "=", str(x+y))

def subtract():
    print("Subtract two numbers:")
    x = int(input("1st number\n>"))
    y = int(input("2nd number\n>"))
    print(str(x), "-", str(y), "=", str(x - y))

def multiply():
    print("Multiply two numbers:")
    x = int(input("1st number\n>"))
    y = int(input("2nd number\n>"))
    print(str(x), "*", str(y), "=", str(x * y))

def divide():
    print("Divide two numbers:")
    x = int(input("1st number\n>"))
    y = int(input("2nd number\n>"))
    print(str(x), "/", str(y), "=", str(x / y))

def modulus():
    print("Divide two numbers by modulus:")
    x = int(input("1st number\n>"))
    y = int(input("2nd number\n>"))
    print(str(x), "/", str(y), "=", str(x % y))

def exponent():
    print("the first number to the power of the second:")
    x = int(input("1st number\n>"))
    y = int(input("2nd number\n>"))
    print(str(x), "^", str(y), "=", str(x ** y))

def floor_division():
    print("Divide and round down to the nearest integer:")
    x = int(input("1st number\n>"))
    y = int(input("2nd number\n>"))
    print(str(x), "/", str(y), "=", str(x // y))

add()
subtract()
multiply()
divide()
modulus()
exponent()
floor_division()
