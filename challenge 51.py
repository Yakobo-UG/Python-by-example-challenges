#Using the song “10 green bottles”, display the lines “There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. Then ask the question “how many green bottles will be hanging on the wall?” If the user answers correctly, display the message “There will be [num] green bottles hanging on the wall”. If they answer incorrectly, display the message “No, try again” until they get it right. When the number of green bottles gets down to 0, display the message “There are no more green bottles hanging on the wall”
bottles = 10
print("There are", bottles," green bottles hanging on the wall,",  bottles, " green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
while bottles == 10:
    bottles = bottles -1
    ask = int(input("how many green bottles will be hanging on the wall?: "))
    if ask == bottles:
        print("There will be",  bottles, " green bottles hanging on the wall")
    else:
        while ask != bottles:
            print("No, try again")
            ask = int(input("how many green bottles will be hanging on the wall?: "))


            #failed to solve this one


