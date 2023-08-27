print("Welcome to Treasure Island\nYou mission is to find the treasure")

print("You are on the crossroad")
left_or_right = input("Which way you want to go? left or right\n").lower()

if left_or_right == "right":
    print("Game is over")

else:
    print("There is a pond in front of you")
    swim_or_wait = input("What are you going to do? swim or wait\n").lower()

    if swim_or_wait == "swim":
        print("Game is over")

    else:
        print("There are doors in front of you")
        door_color = input(
            "Which color's of door you want to open? red or yellow or blue\n").lower()

        if (door_color != 'yellow'):
            print("Game is over")
        else:
            print("You are survived!")
