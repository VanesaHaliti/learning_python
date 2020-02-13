# Immutability

name = "Sam"
# we cant do this since String are immutable -> name[0] = "P"
# We basically have to create a new string
last_letters = name[1:]
print("P" + last_letters)

#   String multiplication

letter = "z"
print(letter * 10)

# Methods
x = "Hello World"
print(x.upper())
print(x.lower())
print(x.split()) # splits the sentence based on the white space by default
print (x.split("o"))