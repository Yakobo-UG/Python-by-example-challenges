#Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result. 
Name_low = str(input("Enter first name in lower case: "))
Name_low1 = str(input("Enter Surname name in lower case: "))
title = Name_low.title()
title1 = Name_low1.title()
print(title + " " + title1)