
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
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong! ❌ The correct answer is: {correct_answer[0].capitalize()}")

#* Printing the game with the for it makes 
for questions in questions_python:
    print("\n---------------------------------------")  # make a space 
    ask_question_py(
        questions["question"], 
        questions["choices"], 
        questions["correct_answer"]
    )

print("\n---------------------------------------") 
print(f"Your final score is: {score} out of 10")