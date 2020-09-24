
# Initializing, importing and seeding the random number generator

from random import seed
from random import randint
seed(1)

# Introduction to the name of the project

# Defining a Constant - Name of Project
projectName = 'Organizational Onboarding System'

print('**********Welcome to the ', projectName,'**********','\n')

print('Please fill out the required information in order to help us properly onboard you into our organization.')

# Creating a bool for Program state. While the bool is set to true the program will continue to loop

programState = True

# Defining the questions to ask the new hire by defining a function.

def QuestionFunction():

# Receiving a series of inputs to create a profile on the new hire.

    firstName = input('What is your First Name?')
    lastName = input('What is your Last Name?')
    age = input('How old are you?')
    department = input('Which department will you be working in?')
    contactNumber = input('What is a good 10 digit contact number for you?')
    email = input('What is your email address?')

# Creating a list to store user profile information.

    userProfile = [firstName, lastName, age, department, contactNumber, email]

# Iterating over the list created so the users can verify if the information entered is correct or not.

    for x in userProfile:
        print(x)

# I've commented out an alternate way of displaying the entered information without using a list. It looks cleaner as it has headers
# but does not utilize a list.
    
    # print('\n','First Name:',firstName,'\n','Last Name:',lastName,'\n','Age:',age,'\n','Department:',department,'\n','Contact Number:',contactNumber,'\n','Email:',email,'\n')

# The below code segment queries the user if the information entered is correct or not and depending on their selection either returns them
# to the main menu or allows them to re-enter their information.

    correctQuery = input('Is the above information correct? Press y or n...')

    if correctQuery == 'y':
        print('Thank you for filling out your information.')

    elif correctQuery == 'n':
        print('\n','Please re-enter your information.','\n')
        QuestionFunction()

    else:
        print('Something has gone wrong. Please re-enter your information.')
        QuestionFunction()

# Creating a while loop. So long as the user selects "y" to the below query and that they do not want to exit the program at a lower
# query than the program will loop back to this location.

while programState == True:

    startQuestioning = input('Would you like to get started filling out your information? Press y or n...')

# If the user selects 'y' above than they are asked to perform a simple calculation to prove that they are a human user.

    if startQuestioning == 'y':

        print('In order to prove you are an actual user please perform this simple calculation:')

# RNG creates 2 integers which are then added together and the sum is checked based of the user input.
# If the user's answer is correct than the user continues through the program.
# If the user's answer is incorrect the program closes.

        num1 = randint(0, 10)
        num2 = randint(0, 10)

        total = num1 + num2

        inputString = "What is {0} + {1} = ?".format(num1, num2)

        userAnswer = int(input(inputString))


        if userAnswer == total:
            print('You have passed the simple calculation test. You may proceed.')

            QuestionFunction()

        elif userAnswer != total:
            print('You are a robot, or really bad at math. Program Terminated.')

            programState = False

        else:
            print('Something has gone wrong. Exiting program.')

            programState = False

# If the user selects that they do not want to start or have already completed their profile they are asked below if they would
# like to exit the program

    elif startQuestioning == 'n':
        
        exitProgramQuery = input('Would you like to exit the program? Press y or n...')
        
        if exitProgramQuery == 'y':
            
            print('********** Now Exiting the ',projectName, '**********')
            
            programState = False
            
        elif exitProgramQuery == 'n':
            print('Returning to Questioning menu.')

        else:
            print('Something has gone wrong. Returning to Questioning menu.')

    else:
        print('Something has gone wrong. Please proceed with filling out the requested information.')
        QuestionFunction()