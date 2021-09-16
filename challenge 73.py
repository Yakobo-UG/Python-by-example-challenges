#Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting from 1. Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list. Sort the remaining data and display the dictionary. 
'''
fruit1 = str(input("Enter your first fruit: "))
fruit2 = str(input("Enter your second fruit: "))
fruit3 = str(input("Enter your third fruit: "))
fruit4 = str(input("Enter your forth fruit: "))
Dic = {
    1 : fruit1,
    2 : fruit2,
    3 : fruit3,
    4 : fruit4,
}
print(Dic)

getRid = int(input("What do you want to get ride: "))
del Dic[getRid]
print(sorted(Dic.values()))
'''
FoodDic = {}
fruit1 = str(input("ENter your first food: "))
FoodDic[1] = fruit1
fruit2 = str(input("ENter your second food: "))
FoodDic[2] = fruit2
fruit3 = str(input("ENter your third food: "))
FoodDic[3] = fruit3
fruit4 = str(input("ENter your forth food: "))
FoodDic[4] = fruit4
print(FoodDic)
getRid = int(input("What do you want to get ride: "))
del FoodDic[getRid]
print(sorted(FoodDic.values()))
