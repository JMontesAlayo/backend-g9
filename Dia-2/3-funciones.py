def sumar(num1, num2):
    return num1 + num2

def sumar_n_numeros(*args):
    # args > arguments sera recibir N (ilimitado) numero de parametros
    print(args)
    # sumar todos los valores de la tupla args utilizando un for
    total = 0
    for numero in args:
        # print(numero)
        total = total + numero
    # return total

    # Usando los numeros de las posiciones
    total2= 0    
    for posicion in range(len(args)):
        # print(posicion)
        total2 = total2 + args[posicion]
    
    print(total2)
    return total

print(sumar(5,10))

resultado = sumar_n_numeros(10,5,18,7,22,56,89)
print(resultado)

resultado = sumar_n_numeros(10,5,18,7,22,56,89,15,14,13,15,18,19,14,17,20)
print(resultado)


def inscribir_personas(persona):
    print(persona)