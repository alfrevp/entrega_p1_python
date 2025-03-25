import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

puntaje =  0.0

questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for question, answer_choices, correct_answer_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer_choices):
        print(f"{i + 1}. {answer}")


    respuesta_correcta = False

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        
        input_usuario = input("Respuesta: ")

        if not input_usuario.isdigit():
            print("Respuesta no valida")
            sys.exit(1)
        
        user_answer = int(input_usuario) - 1

        if user_answer < 0 or user_answer >= len(answer_choices):
            print("Respuesta no valida")
            sys.exit(1)

                # Se verifica si la respuesta es correcta
        if answer_choices[user_answer].strip() == answer_choices[correct_answer_index].strip():
            print("¡Correcto!")
            puntaje += 1
            respuesta_correcta = True
            break
        else:
            print("Incorrecto.")
            puntaje -= 0.5


        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
    if not respuesta_correcta:
        print("Incorrecto. La respuesta correcta es:")
        print(answer_choices[correct_answer_index])

    # Se imprime un blanco al final de la pregunta
    print()

    # para que el puntaje no sea negativo
puntaje = max(0, puntaje)

print(f"Tu puntaje final es {puntaje}")