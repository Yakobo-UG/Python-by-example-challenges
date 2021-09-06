#Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for the number of times they entered. 
'''
Name = str(input("Enter name: "))
num = int(input("Enter number: "))
for i in Name:
    #print(i)
    for p in range(num):
        print(i)
 '''   

Name = str(input("Enter name: "))
num = int(input("Enter number: "))
for i in range(num):
    #print(i)
    for p in Name:
        print(p)




