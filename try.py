
try:
    age = int(input('Enter your age: '))

    faveNum = int(input('What is your favorite number: '))
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
         print('Welcome, you are old enough.')

    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)

except ValueError:
    print("Please give a number")
except ZeroDivisionError:
    ("Please don't put a zero buddy")

finally:
    print("Congrats No Idiot Errors!")