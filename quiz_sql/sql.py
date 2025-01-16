from questions_sql import questions_sql


#getting the promt and assing on name 
name = input("What is your name?: ")
# Welcome message
print("=---------------------------------=")
print(f"            Welcome to the quiz {name}!")
print("     L E T' S   T R Y   Y O U R   K N O W L E D G E")
print("        O F   S Q L   📊 ")
print("=---------------------------------=")

print("=---------------------------------=")  # Jumping line

# Función to print the quuestion and validate if it correct or incorrect
def ask_question_sql(question, choices, correct_answer):
    print(question) 
    for choice in choices:
        print(choice)

    user_answer = input("Enter your answer (number or text): ").lower()
    if user_answer in correct_answer:
        print(f"Correct! {name} ✅")
    else:
      print(f"Wrong!: {name} ❌ The correct answer is: {correct_answer[0].capitalize()} ")

for question_data in questions_sql:
    print("\n---------------------------------------")  # <br>
    #rmb call all the parr at the end to looping 
    ask_question_sql(
        question_data["question"],
        question_data["choices"], 
        question_data["correct_answer"]
    )

 # print("Loaded questions:")
# for question in questions_sql:
#     print(question["question"])       