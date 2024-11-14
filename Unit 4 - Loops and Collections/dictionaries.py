#Dictionaries are a type of collection, like a list
#a list is a collection of items in a sequence
#Dictionaries store data in key-value pairs
# you can retreive data quickly by using a key
#instead of by its index

#create a dictionary

James ={
    "name": "James",
    "age": 15,
    "city": "St. Michael",
    "Favorite SSN": 1234456789,
    "height": 6
}
# each key must be unique
print(James["name"])
print(James.get("city"))

# you can add values
James["country"] = "USA"
#you can modify values
James["age"] = 2300465

#remove entries
James.pop("Favorite SSN")

#iterate through a dictionary using a for loop

for key in James:
    print(key)