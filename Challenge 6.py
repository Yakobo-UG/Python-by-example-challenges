#Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user-friendly format.

Startedwith = int(input("How many slices have you started with: "))
Eaten = int(input("How many slices have you eated: "))
Letfwith = Startedwith-Eaten
print(" You are left with ", Letfwith, "slices of pizza")