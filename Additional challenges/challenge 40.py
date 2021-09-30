#Create a function that takes in a list and returns a list of the accumulating sum.
from itertools import accumulate
lists =[2,4,6,77]
accumulate = list(accumulate(lists))
print(accumulate)


