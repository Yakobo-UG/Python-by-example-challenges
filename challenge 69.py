#Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list) of that item in the tuple.

Names = ("Uganda","Kenya","Tanzania","Rwanda","Ethiopia")
print(Names)
user = str(input("Enter one of the countries seen above: "))

print(Names.index(user))