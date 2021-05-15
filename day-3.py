print("Welcome to Treasure island.\nYour Mission is to find the treasure.")

inputs = ["right", "left", "swim", "wait", "red", "blue", "yellow"]
input1 = input2 = input3 = 0

input1 = input(
    "You're at a crossroad. Where do you want to go? Type 'Left' or 'Right'\n"
).lower()

if input1 == "right":
    print("You got hit by a car. Game over")
    exit

elif input1 == "left":

    input2 = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for the boat. Type 'Swim' to swim across.\n"
    ).lower()
    if input2.lower() == "swim":
        print("You got drowned. Game over")
        exit
    elif input2 == "wait":
        input3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n"
        ).lower()
        if input3 == "red" or input3 == "blue":
            print("You got in a room full of dragons. Game over.")
            exit
        elif input3 == "yellow":
            print("You win!")
            exit
