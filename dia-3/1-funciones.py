
def miFuncion():
    print('Hola mundo')


def suma(a, b):
    return a + b


def comprobarEdad(edad):
    if (edad >= 18) :
        return 'Eres mayor de edad'
    else:
        return 'No eres mayor de edad, no puedes ingresar'
    
# edad = input('Ingrese su edad: ')
# edad = int(edad)
# print(comprobarEdad(edad))

alumnos = ['Eduardo', 'Pepe', 'Jose', 'Miguel', 'Julia', 'Raul']

def buscarNombre():
    if not 'Eduardo' in alumnos:
        return False
    # else:
        #return True
    return True

# primer metodo para hacer el ejercicio ingresando los numeros uno por uno

nombres = []
primer_nombre = input('Ingrese el primer nombre: ')
segundo_nombre = input('Ingrese el segundo nombre: ')
tercer_nombre = input('Ingrese el tercer nombre: ')
cuarto_nombre = input('Ingrese el cuarto nombre: ')

nombres.append(primer_nombre)
nombres.append(segundo_nombre)
nombres.append(tercer_nombre)
nombres.append(cuarto_nombre)

nombre_a_buscar = input('Ingrese el nombre a buscar: ')

def buscarPersona(nombre):
    if nombre in nombres:
        return '{} ha sido encontrado {}'.format(nombre, '😀')
    # return 'No pudimos encontrar a {} {}'.format(nombre, '😢')
    # otro metodo de hacer el format
    return f'No pudimos encontrar a {nombre} {"😢"}' 

# print(buscarPersona(nombre_a_buscar))


# segundo metodo

todos_lo_nombres = input('Ingrese nombres separados por comas: ')

nombre_a_buscar = input('Ingrese el nombre a buscar: ')

def separarNombres(lista_nombres):
    nombres = lista_nombres.split(',')
    return nombres


def buscarPersona(nombre):
    array_nombres = separarNombres(todos_lo_nombres)

    if nombre in array_nombres:
        return '{} ha sido encontrado {}'.format(nombre, '😃')
        
    return f'No pudimos encontrar a {nombre} {"😢"}'

print(buscarPersona(nombre_a_buscar))



