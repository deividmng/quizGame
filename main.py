# Welcome message
print("What is your name?")
name = input("Enter your name: ")

#The f is the same as ``
print(f"Welcome to the quiz {name}!")
print()#jumping line lest sabe same as br

# Initialize score
score = 0

# Question 1
print("What is the capital of France?")
print("1. Berlin")
print("2. Madrid")
print("3. Paris")
print("4. Rome")
print("5. Spain")

# Getting the anser from the user, same as a promt, added . lower in case the user add Paris to prevent error
# we assing the answer of the use into answer1
anwer_1 = input("Enter your answer: ").lower()

# Checking the answer, on two ways i case the user write or add a number
if anwer_1 == "paris" or anwer_1 == "3" :
    print("Correct the capital of France is Paris !")
    score += 1
else:
    print(f"Wrong! The correct answer is Paris, try again {name}")
    

print("Which of the following is not a JavaScript data type?")
print("1. String")
print("2. Boolean")
print("3. Undefined")
print("4. Float")
print("5. Null")    

anwer_2 = input("Enter your answer: ").lower()

# Checking the answer, on two ways i case the user write or add a number
if anwer_2 == "float" or anwer_2 == "4" :
    print(f"Wrong! The correct answer is 'Float', try again {name}.")
    score += 1
else:
    print(f"Wrong! The correct answer is Paris, try again {name}")





# End of the quiz
print()
print(f"Your final score is: {score} of 10")

