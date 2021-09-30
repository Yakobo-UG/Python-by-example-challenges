#You hired three programmers and you (hopefully) pay them. Create a function that takes three numbers (the hourly wage of each programmer) and returns the difference between the highest-paid programmer and the lowest-paid.
def program(one, two, three):
    list = [one,two,three]
    return max(list) - min(list)
print(program(1000,2000,3000))