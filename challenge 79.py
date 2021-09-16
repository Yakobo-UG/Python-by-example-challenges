#Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add it to the end of the nums list and display the list. Once they have entered three numbers, ask them if they still want the last number they entered saved. If they say “no”, remove the last item from the list. Display the list of numbers. 
nums =[]
numberadd = int(input("Enter number: "))
fir = nums.append(numberadd)
again = str(input("do you want to add a number: "))
while again == "y":
    numberadd = int(input("Enter number: "))
    add = nums.append(numberadd)
    print(nums)
    again = str(input("do you want to add a number: "))
    while len(nums) == 3:
        ask = str(input("Do you still want the last number saved: "))
        if ask == "n":
            index = nums.index(numberadd)
            del nums[index]
            print(nums)
        else:
            print(nums)

            #finished tho can still be improved
    