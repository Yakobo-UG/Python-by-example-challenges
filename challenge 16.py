#Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”

weather = str(input("Is it rainy of not?: "))
weather = str.lower(weather)


if  weather == "yes" or weather == "YES" or weather == "Yes" :
    windy_or = str(input("Is it windy or not: "))
    if windy_or == "yes" or windy_or == "YES" or windy_or == "Yes":
        print("Its too windy for an umbrella ")
    else:
        print("Take an umbrella")
else :
    print("Enjoy your day")

    