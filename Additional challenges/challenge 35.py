'''
You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.

e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
'''
even = 0
for i in range(1,100):
    if i%2 == 0:
        even += i 
        
print(even)

    
