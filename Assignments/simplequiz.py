a = input("what is 5 + 3\n>")
b = input("what is the capital of Kiribati\n>").capitalize()
c = input("what is the 31st state to join the union\n>").capitalize()
d = input("what is 6 ^ 4\n>")
e = input("When are we getting the donuts\n>").lower()

aa = a == "8"
bb = b == "Tarawa"
cc = c == "California"
dd = d == "1296"
ee = e == "tomorrow"

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
    print(str(score) + "/5")

tally_score()