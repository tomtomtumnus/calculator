#Created on Fri Jan  3 15:11:36 2020
#simple calculator using python

#relevant functions available to the calculator
functions = ["addition", "subtraction", "multiplication", "division"]

def int_checker(prompt):
    """Checks to make sure that the input is an integer."""
    while True:
        integer = input(prompt)
        try:
            return int(integer)
        except ValueError:
            print("That's not a number!")
            
def function_checker(prompt):
    """checks to make sure a valid function is used"""
    function = input(prompt)
    if function in functions:
        return function
    else:
        print("Not a valid operation.")
        print("Pick addition, subtraction, multiplication, or division.")
        
def zero_divison_check(division):
    try:
        return int(division)
    except ZeroDivisionError:
        print("Error! Divided by zero!")
        
print("Greetings.")
print("I am a calculator.")
print("I can add, subtract, multiply, and divide.")
print("Press 'q' to quit.")

while True:
    #calcutation prompts with loop break for 'q'
    integer_one = int_checker("Pick a first number. ")
    integer_two = int_checker("Pick a second number. ")
    operation = function_checker("Pick an operation. ")
    if operation == 'q':
        break
    
    #function operation and return value
    if operation == "addition":
        answer = integer_one + integer_two
        print(answer)
        
    elif operation == "subtraction": 
        answer2 = integer_one - integer_two
        print(answer2)
        
    elif operation == "multiplication":
        answer3 = integer_one * integer_two
        print(answer3)
        
    elif operation == "division":
        answer4 = integer_one / integer_two
        zero_divison_check(answer4)
        print(answer4)
