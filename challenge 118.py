'''
Define a subprogram that will ask the user to enter a number and save it as the variable “num”. Define another subprogram that will use “num” and count from 1 to that number. 
'''
def Enter_num():
    Num = int(input("Enter number: "))
    return Num

def count_num(Num):
    count = 1
    while count <= Num:
        print(count)
        count = count + 1

def main():
    Num = Enter_num ()
    count_num(Num)

main()

