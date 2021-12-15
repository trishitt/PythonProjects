import random


names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
random_no = random.randint(0,len(names)-1)

print (f"{names[random_no]} is going to buy the meal today!")
