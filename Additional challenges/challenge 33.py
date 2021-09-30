'''
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.
'''
student_heights = [180, 124, 165, 173, 189, 169, 146]
average = sum(student_heights)/len(student_heights)
print(average)