class Persona:
    estatura= 1.55
    peso = 80000
    signo = 'LEO'

# metodos magicos: se reconocen por tener __ al inicio y al final del nombre del metodo
    def __str__(self):
        # el metodo __str__ sirve para indicar que cuando se mande a llamar a la clase a imprimir se modificara la impresion predeterminada que mostraba la ubicacion de memoria por lo que se va a retornar, solamente se puede retornar str
        return 'Bienvenido a la clase Persona'

    def saludar(self):
        # self > en python en todas las funciones dentro de una clase (ahora las funciones pasan a llamarse METODOS) y para que pueda utilizar la propia configuracion de la clase (como sus atributos y otros metodos) se declara como primer parametro la palabra 'self',
        # el parametro self NUNCA se pasara como parametro fuera de la clase
        texto = 'Hola soy una persona y mido ' + str(self.estatura)
        print(texto)

    def saludar_cordialmente(self, nombre):
        texto = 'Hola {}, mucho gusto.'.format(nombre)
        return texto
        



# variable > instancia de la clase
jean = Persona()
gabriela = Persona()
jean.estatura = 1.65
gabriela.estatura = 1.60


# retorna el nombre de la clase en formato string
print(Persona.__name__) # Persona
print(jean)
print(jean.estatura)
print(gabriela.estatura)

jean.saludar()
gabriela.saludar()

resultado = jean.saludar_cordialmente('gabriela')

print(resultado)

