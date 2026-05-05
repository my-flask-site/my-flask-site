import datetime

name = input("What is your name? ")

hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(greeting + ", " + name)	
