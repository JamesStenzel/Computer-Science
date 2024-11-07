# there is more than one type of lopp in python
#for loops let you iterate through a list
# -great for looping a set number of times
# what if we need to loop an uncertain number of times
#e.g. entering your password
#could be right the first tome
#could take a million tries

x = 0
real_pass = "potato45"
entered_pass = ""
while real_pass != entered_pass:
    entered_pass = input("Plaese enter the password\n> ")
    if real_pass != entered_pass:
        print("Incorrect password, try again")
        x += 1
        print(str(x)+" attempts")
print("Acces Granted. Welcome!")
print(x)

#with while loops, you need to be careful of infinite loops
#when your PC is in sleep mode, it has nightmares about infinite loops
#example (Do not enter)
count = 0
for x in range(0,5):
    count += 1
    print(count)

#Real world example
#type exit to quit

user_input = ""

while user_input != "exit":
    user_input = input("Enter something")
print("All Done")