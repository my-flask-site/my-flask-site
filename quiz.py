print("Welcome to the Python Quiz Game!")
print("-------------------------------")

score = 0

# Question 1
answer = input("1. What is the capital of Nigeria? ")
if answer.lower() == "abuja":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Abuja")

# Question 2
answer = input("2. What is 5 + 3? ")
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 8")

# Question 3
answer = input("3. What language are we learning? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! It's Python")

print("-------------------------------")
print("Your score is:", score, "/ 3")	
