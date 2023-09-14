'''  this code plays a game , assume we are in a resturant to eat lunch
 afterwords we all put our credit card in a plate, whosever credit card is picked up 
 the server will pay for everybodys lunches.

 '''
import random

# spliting names and puting in a list 

name_string = input("Give me everybodis name seperated by comma")
names = name_string.split(",")
# getting the total item in the list

num_items = len(names)
# now we generate random number between 0 and the last item index.
random_choice = random.randint(0, num_items -1)

# pick out random person name from the list of names using the random number

peroson_who_pay = names[random_choice]
print(peroson_who_pay + "is going to pay !")


