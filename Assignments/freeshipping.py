# free shipping eligibility
# prime member OR purchase of over $25
# if under 18, you need parent consent

def free_shipping(ps,pa,age,consent):
    if (ps == True or pa >= 25) and (age >= 18 or consent == True):
        print("free shipping")
    else:
        print("ineligible for free shipping")

p = False
c = 290
a = 93
con = False

free_shipping(p,c,a,con)