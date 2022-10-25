numeros = [4, 5, 8, 3, 2, 1, 9]

for numero in numeros:
    # print(numero)
    pass # pass es solo para que pase el bucle no produce nada


alumnos = ['Jose', 'Miguel', 'Raul', 'Eduardo', 'Jorge']

for index, alumno in enumerate(alumnos):
    if index == 2:
        # pass
        # break
        continue
    print(index, alumno)


# persona = {
#     'nombre': 'jean', 
#     'apellido': 'montes'
# }

# for nombre, apellido in persona.items():
#     print(nombre, apellido)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']

# for q, a in zip(questions, answers):
#     print('What is your {}?  It is {}.'.format(q, a))

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


