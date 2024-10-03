# 2 functions
print()
input("please enter username\n>")   #\n is an escape character
                                    #\n starts a new line

#conversion functions
str()
int()
float()
bin()
bool()

#stuff in between parenthesis is a PARAMETER


#variables
#syntax
# <name> = <value>
x = 5

#snake case - all lowercase, underscore for spaces
#concise - short and descriptive
username = "owsowski"       #define str
fav_animal = "Calugo"       #define str
total_poptarts = 12         #define int
percent_complete = 23.52    #define float
is_cool = True              #define boolean
first_letter = 'c'          #define character

total_poptarts = 8

#arithmetic operators
# + - * / ** % //
print(4 + 4)            #8
print("4" + "4")        #44
print("cat" + "dog")    #catdog
print("cat" * 3)        #catcatcat
print("cat" + 3)        #error

#working programs
#1. add two numbers using input
x = int(input("what is x?\n>"))
y = int(input("what is y?\n>"))
print(x + y)

#2. converts celsius to fahrenheit
temp_celsius = 40
temp_fahrenheit = (temp_celsius * 1.8) + 32
print(temp_celsius + " degrees c equals " + temp_fahrenheit + " degrees f.")

#functions
#functions are a lot like variables
#they have names
#can be called from memory by name
#store information
def potato():           #def keyword + name + ():
    print("potato")     #lines indented are inside the function

#functions are not ran when defined, and must be called to run
potato()    #every function must have parenthesis even if it has no parameters

def jump(how_high):
    print("you jumped", str(how_high), "inches!")

jump(14)

def make_a_word(a,b,c,d,e,f,g,h,i,j,k):
    print(str(a+b+c+d+e+f+g+h+i+j+k))

make_a_word("z","a","c","k","o","s","o","w","s","k","i")

def top_ten_games():
    print("1. elden ring")
    print("2. shadow of the colossus")
    print("3. minecraft")
    print("4. diablo 3")
    print("5. gran turismo 7")
    print("6. overwatch")
    print("7. ratchet & clank: up your arsenal")
    print("8. world of warcraft")
    print("9. path of exile")
    print("10. enter the gungeon")

#scope
#global and local variables
#global - defined at no indentation level
#local - defined inside of a function

#global variables can be used anywhere in the program
todd = "cool guy"   #global

#local variables can only be used in the function they are created in
def my_function():      
    smith = "not a cool guy"    #local
    todd = "strange guy"        #local, even though it has the same name
    print(todd)                 #prints the local variable
    #searches for local variables first

def my_function2():
    global todd             #tells the function to refer to the global todd
    todd = "strange guy"    #reassigning tod - global

#return functions
#functions can return values
#value is sent to where the function was calle
#function does its work, and returns something

def add2(x,y):
    return x + y    #returns the sum of x and y to where the function was called

answer = add2(2,10)
print(answer)