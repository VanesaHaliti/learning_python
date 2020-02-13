def fileExercise():
    
    name = input('Enter file name: ')

    while True:
        with open(name, 'a') as f:
            print('Write something or press Exit to exit: ')

            x = input()
            if x == 'Exit':
                break
            else:
                f.write('You will get the job!')
        
        with open(name, 'r') as f:
            line = f.readline()
            print(line)


fileExercise()

# Write a script that opens a file named 'test.txt', writes 'hello' to the file and then closes it.

with open('test.txt', mode='w') as f:
    f.write('hello')
    