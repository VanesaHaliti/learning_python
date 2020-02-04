#1. Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print("Watch out! An error occurred!")

#2. Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done'

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Whoops! Can't devide by zero")
finally:
    print("All done!")

#3. Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            number = int(input("Please enter an integer: "))
        except:
            print("An error occurred! Please try again.")
            continue
        else:
            break
    print("Thank you for providing an integer. Your number squared is ", number ** 2)

ask()

