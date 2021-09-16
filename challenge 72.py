#Create a list of six school subjects. Ask the user which of these subjects they don’t like. Delete the subject they have chosen from the list before you display the list again.
subjects = ["Math","Physic","biology","TD","English","chemistry"]
print(subjects)
user = str(input("Enter the subject you hate: "))
index = subjects.index(user)
del subjects[index]
print(subjects)