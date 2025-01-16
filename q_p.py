
# Importing the question data from another file
from questions_data import questions_data
# Welcome message
print("=---------------------------------=")
print("     L E T' S   T R Y   Y O U R   K N O W L E D G E")
print("        O F   P Y T H O N   🐍 ")
print("=---------------------------------=")

print("What is your name?")
#getting the promt and assing on name 
name = input("Enter your name: ")

# The f-string is a way to insert variables into strings
print(f"Welcome to the quiz {name}!")
print()  # Jumping line

#importing the josn from questions_python.py same as a import from
from questions_python import questions_python 
score = 0
# This function have 3 parr the same a are in in the json "obj"
#* I'm getting the score on global 
def ask_question_py(question, choices, correct_answer):
    global score
    print(question)
    for choice in choices:  # Mostrar las opciones de cada pregunta
        print(choice)
    
    user_answer = input("Enter your answer (number or text): ").lower()# 

    # Verificar si la respuesta del usuario está en las respuestas correctas
    if user_answer in correct_answer:
        print(f"Correct! {name} ✅")
        score += 1
    else:
        #using {correct_answer[0].capitalize()} i get inti the correct_answer as I have 2 the num and the str 
        print(f"Wrong!: {name} ❌ The correct answer is: {correct_answer[0].capitalize()} ")

#* Printing the game with the for it makes 
for questions in questions_python:
    print("\n---------------------------------------")  # make a space 
    ask_question_py(
        questions["question"], 
        questions["choices"], 
        questions["correct_answer"]
    )

print("\n---------------------------------------") 
print(f"Your final score {name} is: {score} out of 10")