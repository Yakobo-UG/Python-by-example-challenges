#Using program 100, ask the user for a name and a region. Display the relevant data. Ask the user for the name and region of data they want to change and allow them to make the alteration to the sales figure. Display the sales for all regions for the name they choose. 

'''
        N   S   E   W
John    23  65  87  56
Tom     87  22  77  99
Peter   73  00  83  27
Fiona   11  73  27  89

'''

Dic2D = {"N": {"John":  23,  "Tom": 87 , "Peter": 73 , "Fiona": 11 },
"S": { "John":65, "Tom":22, "Peter":00, "Fiona":73}, 
"E": { "John": 87, "Tom": 77, "Peter":83, "Fiona":27},
"W": { "John": 56, "Tom": 99, "Peter":27, "Fiona":89}}

askName = input("Enter name: ")
askRegion = input("Enter region: ")
print(Dic2D[askRegion][askName])
NewValue = int(input("Enter new value: "))
Dic2D[askRegion][askName] = NewValue
print(Dic2D[askRegion])