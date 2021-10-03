'''
Define a subprogram that will ask the user to pick a low and a high number, and then generate a random number between those two values and store it in a variable called “comp_num”. 
 
Define another subprogram that will give the instruction “I am thinking of a number...” and then ask the user to guess the number they are thinking of.  
 
Define a third subprogram that will check to see if the comp_num is the same as the user’s guess. If it is, it should display the message “Correct, you win”, otherwise it should keep looping, telling the user if they are too low or too high and asking them to guess again until they guess correctly.

'''
import random
def Low_high():
    up = int(input("Enter a low number: "))
    down = int(input("Enter a high number: "))
    comp_num = random.randint(up,down)
    return comp_num
def guess_num():
    guess = int(input("I am thinking of a number, what is the number: "))
    return guess
def check(comp_num, guess):
    try_agian = True
    while try_agian == True: 
        if comp_num == guess:
            print("Correct, you win")
            try_agian == False
        elif comp_num > guess: 
            print("Too high try again")
            try_agian = True
            guess = int(input("I am thinking of a number, what is the number: "))
            
        elif comp_num < guess:
            print("Too low try agian")
            try_agian = True
            guess = int(input("I am thinking of a number, what is the number: "))
            
def main():
    comp_num = Low_high()
    guess = guess_num()
    check(comp_num,guess)
main()

        

