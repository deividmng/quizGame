# here is where I gonna create the quuestion and the choices and aswer
#* Importando sqlite3 con el alias sql
import sqlite3 as sql
#* Conexión a la base de datos
def connect_to_db():

    # Conectting or creating the baseDate 
    connection = sql.connect("question.db")
    return connection

#* Crear la tabla si no existe
def create_table(connection):
    cursor = connection.cursor()
    # Create the table question in case is not existid 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            choice_1 TEXT,
            choice_2 TEXT,
            choice_3 TEXT,
            choice_4 TEXT,
            correct_answer TEXT
        )
    """)
    connection.commit()
    print("Table create sucefully.")
    
    
#* Insert a new table on question
def insert_question(connection, question, choices, correct_answers):
    cursor = connection.cursor()
    # Conmver the question into a string adding ,
    correct_answer_str = ", ".join(correct_answers)
    
    cursor.execute("""
        INSERT INTO questions (question, choice_1, choice_2, choice_3, choice_4, correct_answer) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (question, choices[0], choices[1], choices[2], choices[3], correct_answer_str))
    
    connection.commit()  # commit the changes 
    print(f"Question '{question}' Added suceffuly.")

#* update a question that exists alredy 
def update_question(connection, question_id, new_question=None, new_choices=None, new_correct_answers=None):
    cursor = connection.cursor()

    # apdate the text if we added 
    if new_question:
        cursor.execute("UPDATE questions SET question = ? WHERE id = ?", (new_question, question_id))
    
    # Act the opction 
    if new_choices:
        cursor.execute("""
            UPDATE questions 
            SET choice_1 = ?, choice_2 = ?, choice_3 = ?, choice_4 = ? 
            WHERE id = ?
        """, (new_choices[0], new_choices[1], new_choices[2], new_choices[3], question_id))
    
    # Act the question if all are correct 
    if new_correct_answers:
        correct_answer_str = ", ".join(new_correct_answers)
        cursor.execute("UPDATE questions SET correct_answer = ? WHERE id = ?", (correct_answer_str, question_id))
    
    connection.commit()  # add the changes
    print(f"Pregunta con id {question_id} actualizada correctamente.")

#* Eliminar una pregunta por su ID
def delete_question(connection, question_id):
    cursor = connection.cursor()
    
    # Eject tje quuestion to delete and ask 
    cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))
    
    connection.commit()  # add the changes
    print(f"Pregunta con ID {question_id} eliminada correctamente.")

#* The word __main__ is not an arbitrary name; it is a special convention in Python.
if __name__ == "__main__":
    # Conectar a la base de datos
    connection = connect_to_db()
    # Crear la tabla
    create_table(connection)
    
    #! Insert a new question
    #* remenber as we gonna passs the parr call them before to call the fuction 
    # question = "What does 'HTML' stand for?"
    # choices = ["HyperText Markup Language", "HighText Markup Language", "HyperTabular Markup Language", "None of the above"]
    # correct_answers = ["1", "hypertext markup language"]
    # insert_question(connection, question, choices, correct_answers)


    
    # !Actualizar la pregunta
    # update_question(connection, 3, 
    #                 new_question="In Python, which function is used to get the length of a list?", 
    #                 new_choices=["len()", "size()", "count()", "length()"], 
    #                 new_correct_answers=["1", "len"])  # Respuesta correcta: opción 3
    
    # Eliminar la pregunta
   
   #! Eliminar la pregunta
  #!Solicitar al usuario el ID de la pregunta a eliminar
  
    # user_answer_delete = input("Enter the ID of the question you want to delete: ")
    
    # # Validar la entrada del usuario
    # if user_answer_delete.isdigit():  # Comprobar si el usuario ingresó un número
    #     question_id = int(user_answer_delete)
    #     delete_question(connection, question_id)  # Llamar a la función con el ID proporcionado
    # else:
    #     print("Invalid input. Please enter a valid number.")



    
    # Cerrar la conexión
    connection.close()
