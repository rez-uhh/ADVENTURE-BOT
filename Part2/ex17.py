import random
adjective = ['Witty', 'Charming', 'Swift', 'Fierce', 'Gentle', 'Mighty']
animal = ['Monkey', 'Fox', 'Snake', 'Chicken', 'Panda', 'Tiger']
print("What's your name?")
name = input()
print(name + ", " + "your codename is " + random.choice(adjective) + " " + random.choice(animal) + "!")

print("Anddd... Your lucky number is... " + str(random.randrange(1, 99)) + "!")