# and, or, !

def chk_eleg(age,exp):
    #you need to be at least 18 and have at least 1 year of experience
    if age >= 18 and exp >= 1:
        print("eligible")
    else:
        print("not eligible")

a = int(input("Age\n>"))
b = int(input("Years of Experience\n>"))
chk_eleg(a,b)