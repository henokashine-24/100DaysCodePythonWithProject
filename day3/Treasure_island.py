# in this exercise we are hunting treasure 
print("\n")
print("Welcome to the treasure island \n")
print("Your mission is to find the Treasure!\n ")
choice1 = input('You\'re at the cross road.Where do you want to go? Type "left" or "right" \n' ).lower()
if choice1 == "right":
    print("there is no road this way. Game over for you.")
if choice1 == "left":
    choice2 = input('You\'ve come to the lake.There is an island in the middle of the lake. Type "wait" to wait for a boat.Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 =input('You arrived at island unharmed.There is a house with three doors.One red, one yellow and one blue.which color do you choose? \n').lower()
        if choice3 == "red":
            print("Fire house. Game Over \n")
        elif choice3 == "yellow":
            print("You found the reasure. You won\n")
        elif choice3 == "blue":
            own = input("what would like to do in the blue house as ther is a lot of things to do? type 'up' to go up and type 'down' to down").lower()
            if own == "up":
                print("go to the upstairs and there you will find your suprprise!")
            else:
                print("your suprise is waiting for you in down staris!")
        else:
            print("Please type the choice given. red, yellow and blue")

            # this is code is modifed a bit. 