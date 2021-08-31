#Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format. 

HighNo = int(input("Enter a number above 100: "))
LowNo = int(input("Enter a number below 10: "))
Notimes =  HighNo/LowNo
print(LowNo, "go into", HighNo, Notimes, "number of times")