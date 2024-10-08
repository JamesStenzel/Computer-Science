a = input("what is 5 + 3\n>")
b = input("what is the capital of Kiribati\n>")
c = input("what is the 31st state to join the union\n>")
d = input("what is 6 ^ 4\n>")
e = input("what is the name of the can of dog food in back to the future\n>") # kal kan

aa = a == "8"
bb = b == "Tarawa"
cc = c == "California"
dd = d == "1296"
ee = e == "Kal Kan"

def tally_score():
    global score
    score = 0
    if aa == True:
        score += 1
    if bb == True:
        score += 1
    if cc == True:
        score += 1
    if dd == True:
        score += 1
    if ee == True:
        score += 1

tally_score()
print(str(score) + "/5")
