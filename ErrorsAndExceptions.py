# three keywords: try, except, finally
''' def add(n1, n2):
    print(n1 + n2)
'''

'''number1 = 10
number2 = input("Please provide a number: ") #it gives a string so we have an error
add(number1, number2)
'''
try:
    result = 10 + 10
    # result = 10 + '10' -->error
except:
    print("Hey, it looks like you aren't adding correctly!")
else:
    print("All went well!")
    print(result)

print("------------")

try:
    f = open('testfile', 'w')
    f.write = 'Write a test line'
except TypeError:
    print("There was a type error")
except OSError:  # its a build in exception
    print("Hey, you have an OS error!")
finally:  # Executes always no matter what
    print("I always run!")

print("------------")


def ask_for_int():
    while True:  # when we use While we should use a break somewhere
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops!That's not a number")
            continue
        else:
            print("Yes, thank you!")
            break
        finally:
            print("End of try/except/finally")


ask_for_int()
