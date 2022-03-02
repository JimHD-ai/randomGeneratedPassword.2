import string
import random

"""We make a generator that created a random password without any 
conditions, now we will put some conditions so that the password is 
 more to our standards"""

#We need to create different lists for all the different characters or special characers and digits

upperCaseLetters = list(string.ascii_uppercase)
lowerCaseLetters = list(string.ascii_lowercase)
digits = list(string.digits)
specialCharacters = list("!@#$%^&*()")

#Now we need to ask the user for the length of the password
#And how many of the different characters/digits/specials he wants
#The sum of which isn't greater from the total length of the password
def randomGeneratedPassword():
    length = int(input("Enter the length of the password: "))
    lengthUpper = int(input("Enter how many uppercase letters you want: "))
    lengthLower = int(input("Enter hot many lowercase letters you want: "))
    lengthDigits = int(input("Enter how many digits you want: "))
    lengthSpecial = int(input("Enter how many special characters you want: "))

    contitionLength = lengthDigits + lengthSpecial + lengthLower + lengthUpper

    if length < contitionLength:
        print("Error: Total number of conditions exceed the length of the password!!")
        return

#Begin creating the password
    password = []

#Setting the conditions
    for i in range(lengthUpper):
        password.append(random.choice(upperCaseLetters))
    for i in range(lengthLower):
        password.append(random.choice(lowerCaseLetters))
    for i in range(lengthDigits):
        password.append(random.choice(digits))
    for i in range(lengthSpecial):
        password.append(random.choice(specialCharacters))

    #print the password
    random.shuffle(password)
    print(''.join(password))

randomGeneratedPassword()