# Importing the question data from another file
from questions_data import questions_data
# Welcome message
print("=---------------------------------=")
print("     L E T' S   T R Y   Y O U R   K N O W L E D G E")
print("        O F   J A V A S C R I P T   💻 ")
print("=---------------------------------=")


print("What is your name?")
#getting the promt and assing on name 
name = input("Enter your name: ")

# The f-string is a way to insert variables into strings
print(f"Welcome to the quiz {name}!")
print()  # Jumping line

# Initialize score
score = 0

# Function to ask questions and check answers with 3 parrmater 
def ask_question(question, choices, correct_answer):
    global score  # Accessing the score variable "scope"
    print(question)
    #with this  for in  I display the choices
    for choice in choices:
        print(choice)  # Show the choices
     #Here we are getting the user_answer, and we assing on user_anwer andded the .lower to make the
     #choineces on lowerCase to prevent error    
    user_answer = input("Enter your answer: ").lower()  # Normalize to lower case

    # Check if the answer is correct, can use the number as well as in the data it have multipe choice 
    if (correct_answer):  # If correct_answer is a list, .."correct_answer": ["paris", "3"]
        #in "choices": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome", "5. London"],
        # with this if else I compare in case I and the num 3 str comber a string 
        if user_answer in correct_answer or user_answer in [str(choices.index(choice) + 1)
                for choice in choices if correct_answer[0].lower() in choice.lower()]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer[0]}. Try again {name}.")
    else:
        # If correct_answer is a string (for single correct answers), check both text and number
        if user_answer == correct_answer or user_answer == str(choices.index(f"1. {correct_answer}") + 1):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}. Try again {name}.")


# Ask all questions
for question_data in questions_data:
    ask_question(question_data["question"], question_data["choices"], question_data["correct_answer"])

# End of the quiz
print()
print(f"Your final score is: {score} out of 10")
