'''#Ez task
emri = input("first_name: ")
mbiemri = input("last_name: ")
vendi = input("city: ")
email = input("email: ")
mosha = input("age: ")

print("----------------------")

print("User info: " + "\n" + "First name: " + first_name + "\n" + "Last name:" + last_name + "\n" + "City: " + city + "\n" + "Email: " + email + "\n" + "Age: " + age)'''



# lower and upper methods
myString = "Hello"

print(myString.lower())
print(myString)

print(myString.upper())

#split method
myString = "Hello World"
print(myString.split("W"))

#metoda len() to check the length of a string. Includes spaces
myString = "Hello World"
print(len(myString))

# metoda title to capitalize the first letter of every word
myString = "hello world"
print(myString.title())

# metoda find returns the index of the first occurrence of e
myString = "hello"
print(myString.find('e'))

# String Formatting
name = "Vanesa"
age = 20
print(f"She said her name is {name}")
print(f"She said her name is {name} and she is {age}")
#Or
name = "Vanesa"
age = 20
print("She said her name is " + name)
print("She said her name is " + name + " and she is " + str(age))
