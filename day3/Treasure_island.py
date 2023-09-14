# in this exercise we are hunting treasure 

print("Welcome to the treasure island \n")
print("Your mission is the find the Treasure!\n ")

left_right = input("You are the cross road. where do you want to go? type 'left' or type 'right' \n")
if left_right == "left":
    wait_swim = input("You come to the lake. There is an island in the middle of the lake.. type 'wait' to wait for the boat or type 'swim' to swim across \n")
    if wait_swim == "wait":
        ryb= input("You are arrived at island unharmed.There is a house with 3 doors. one red , one yellow and one blue.which color do you choose? \n")
        if ryb == "blue":
            print("You enter the room of beasts. Game over.")
        elif ryb =="red":
            print("You are the at red house and you are safe..")
        else:
            print("you are at the yellow house and you are safe as well . ")
    else:
        print("Game over for you as you are going to be devoured by the crocdiale in the lake!")
else:
    print("Game Over for you as you pick right. ")
