#Create a list containing the titles of four TV programmes and display them on separate lines. Ask the user to enter another show and a position they want it inserted into the list. Display the list again, showing all five TV programmes in their new positions. 

Tv = ["gamers,","hackers,","builders,","shakers,"]
for i in Tv:
    print(i)

show = str(input("ENter another show: "))
position = int(input("ENter the position you want: "))
new = Tv.insert(position, show)
print(Tv)