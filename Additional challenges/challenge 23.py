#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8'''
Num = input("Enter two digit number: ")
try: 
    separate = int(Num[0]) + int(Num[1])
    print(separate)
except:
    print("Not a 2 digit number")
