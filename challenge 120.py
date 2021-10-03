'''
Display the following menu to the user: 
 1) Addition
 2) Subtraction
Enter 1 or 2
 
If they enter a 1, it should run a subprogram that will generate two random numbers between 5 and 20, and ask the user to add them together. Work out the correct answer and return both the user’s answer and the correct answer. 
 
If they entered 2 as their selection on the menu, it should run a subprogram that will generate one number between 25 and 50 and another number between 1 and 25 and ask them to work out num1 minus num2. This way they will not have to worry about negative answers. Return both the user’s answer and the correct answer. 
 
Create another subprogram that will check if the user’s answer matches the actual answer. If it does, display “Correct”, otherwise display a message that will say “Incorrect, the answer is” and display the real answer. 
 
If they do not select a relevant option on the first menu you should display a suitable message. 
'''
import random
def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    actual = num1 + num2
    print("What is ", num1 ,"+ ", num2, "_____")
    user_answer = int(input("Enter your answer here: "))
    answers = (user_answer, actual)
    return answers

def subtraction():
    num3 = random.randint(25,50)
    num4 = random.randint(1,25)
    actual =  num3 - num4
    print("What is ", num3 ,"- ", num4, "_____")
    user_answer = int(input("Enter your answer here: "))
    answers = (user_answer, actual)
    return answers

def check(user_answer, actual):
    if user_answer == actual:
        print("Its correct")
    else:
        print("Incorrect, the answer is ", actual)

def main():
    print("Display the following menu to the user: \n 1) Addition \n 2) Subtraction ")
    Option = int(input("Enter option 1/2: "))
    if Option == 1:
        user_answer, actual = addition()
        check(user_answer, actual)
    elif Option == 2:
        user_answer, actual = subtraction()
        check(user_answer, actual)
    else:
        print("Incorrect option")
    
main()

