'''
Create a program that will allow the user to easily manage a list of names. You should display a menu that will allow them to add a name to the list, change a name in the list, delete a name from the list or view all the names in the list. There should also be a menu option to allow the user to end the program. If they select an option that is not 
relevant, then it should display a suitable message. After they have made a selection to either add a name, change a name, delete a name or view all the names, they should see the menu again without having to restart the program. The program should be made as easy to use as possible.
'''
list = []
def add_name():
    name1 = str(input("Enter name: "))
    names = list.append(name1)
    return names

def  change_name():
    names = str(input("Enter name you want to change from list: "))
    name2 = str(input("Enter new name: "))
    names.index(names) = name2
    return  names

def delete_name():
    names = str(input("Enter name you want to change from list: "))
    del(names)
    return names
def  view(names):
    print(names)

main()


#got stuck here big time, need more practice on subprogrames






