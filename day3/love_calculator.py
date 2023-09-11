print("Welcome to Love Calculator! \n ")
name1 = input("what is your name? \n ")
name2 = input("what is their name \n ")
combined_string = name1 + name2
lower_case = combined_string.lower()

t=name1.count("t")
r=name1.count("r")
u=name1.count("u")
e=name1.count("e")
true = t+r+u+e
l=name1.count("l")
o=name1.count("o")
v=name1.count("v")
e=name1.count("e")
love = l+o+v+e

love_score = str(love)+ str(true)

print(f"there are :{love_score} characters in these names")


