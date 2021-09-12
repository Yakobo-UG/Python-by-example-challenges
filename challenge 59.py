#Display five colours and ask the user to pick one. If they pick the same as the program has chosen, say “Well done”, otherwise display a witty answer which involves the correct colour, e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”. Ask them to guess again; if they have still not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly
import random
colors = random.choice(["Red","Black","Yellow","Blue", "Pink"])
PickOne = str(input("Enter color you like: "))
if PickOne == colors:
    print("Well done")
else:
    while PickOne != colors:
        print("I bet you are", colors," with envy")
        PickOne = str(input("Enter color you like: "))
    else:
        print("Well done")
