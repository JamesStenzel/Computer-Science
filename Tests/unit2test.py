print("Provide 3 random words to be concatenated")
word_1 = str(input("1st random word\n>"))
word_2 = str(input("2nd random word\n>"))
word_3 = str(input("3rd random word\n>"))
print(word_1 , word_2 , word_3)

def add_three(x,y,z):
    print(int(x)+int(y)+int(z))

num_1 = input("1st number\n>")
num_2 = input("2nd number\n>")
num_3 = input("3rd number\n>")

add_three(num_1,num_2,num_3)

def data_three():
    str_1 = str(input("Write one word\n>"))
    int_1 = int(input("Write one integer\n>"))
    float_1 = float(input("Write one float\n>"))
    int_float = int_1 + float_1
    print(str(int_float),str_1)

