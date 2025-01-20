import sqlite3 as sql

#* Conectar a la base de datos
def connect_to_db():
    connection = sql.connect("question.db")
    return connection

#* Obtener las preguntas de la base de datos
def get_questions_from_db(connection):
    cursor = connection.cursor()
    
    # Consultar todas las preguntas de la tabla
    cursor.execute("SELECT id, question, choice_1, choice_2, choice_3, choice_4, correct_answer FROM questions")
    
    # Obtener todos los resultados
    rows = cursor.fetchall()
    
    # Crear una lista de preguntas con formato adecuado
    questions = []
    for row in rows:
        question_data = {
            "id": row[0],
            "question": row[1],
            "choices": [row[2], row[3], row[4], row[5]],  # Las opciones de respuesta
            "correct_answer": row[6].split(", ")  # La respuesta correcta separada por comas
        }
        questions.append(question_data)
    
    return questions

score = 0

# Función para imprimir la pregunta y validar la respuesta
def ask_question_sql(question, choices, correct_answer):
    global score  # Usamos la variable score global para modificarla dentro de la función

    print(question)  # Imprimir la pregunta
    for index, choice in enumerate(choices, 1):  # Enumerar las opciones
        print(f"{index}. {choice}")  # Mostrar cada opción
    
    user_answer = input("Enter your answer (number or text): ").lower()  # Obtener la respuesta del usuario
    
    # Comprobar si la respuesta es correcta
    if user_answer in correct_answer or (
        user_answer.isdigit() and int(user_answer) in [i + 1 for i in range(len(choices))] and correct_answer[0] == str(int(user_answer))
    ):
        print(f"Correct! ✅")
        score += 1  # Si la respuesta es correcta, sumamos 1 al puntaje
    else:
        print(f"Wrong! ❌ The correct answer is: {correct_answer[0].capitalize()} ")


#* Flujo principal
if __name__ == "__main__":
    # Conectar a la base de datos
    connection = connect_to_db()
    
    # Obtener las preguntas de la base de datos
    questions_sql = get_questions_from_db(connection)
    
    # Obtener el nombre del usuario
    name = input("What is your name?: ")

    # Mensaje de bienvenida
    print("=---------------------------------=")
    print(f"            Welcome to the quiz !")
    print(f"               {name}!")
    print("     L E T' S   T R Y   Y O U R   K N O W L E D G E")
    print("        O F   S Q L   📊 ")
    print("=---------------------------------=")

    # Realizar las preguntas
    for question_data in questions_sql:
        print("\n---------------------------------------")  # Separador
        ask_question_sql(
            question_data["question"],
            question_data["choices"], 
            question_data["correct_answer"]
        )
    
    print("\nYour final score is:", score)
    # # Cerrar la conexión
    # connection.close()
    
