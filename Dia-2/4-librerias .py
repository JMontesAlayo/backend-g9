from camelcase import CamelCase

instancia = CamelCase()

string = 'hola a todos buenas noches y hasta luego'

resultado = instancia.hump(string)

print(resultado)