# una classe es como el plano de una casa

#class Usuario:
#    def __init__(self,nombre,apellido):
#        self.nombre = nombre
#        self.apellido = apellido
#
#    
#    #self hace recibe una referencia a la instancia de la clase
#    def saludo(self):
#        print('hola, mi nombre es:', self.nombre, self.apellido)
#
#
#        
##    nombre = "Roberto"
##    apellido = "Carlos"
#
##aqui tenemos a user como un objeto
#
#user = Usuario('felipe','feliz')
##user2 = Usuario('roberto','carlos')
##print(user.nombre,user.apellido,user2.nombre,user2.apellido)
#user.saludo()
##user2.saludo()
#user.nombre = "Carlos"
#user.saludo()
#
##PARA QUITARLE PROPUEDAS A LAS INSTANCIAS
#del user.nombre
##user.saludo()
#
##PARA ELIMINAR UN USUARIO
#
#del user
##print(user)
#
#
## APLICANDO HERENCIA EN CLASES se utiliza: ()
#class Admin(Usuario):
#    def superSaludo(self):
#        print("Hola me llamo: ",self.nombre, " y soy administrador")
#
#
#admin = Admin('Alonso','Administrador')
#admin.saludo()
#admin.superSaludo()


### EJERCICIO HERENCIA ####

#class Animal:
#    def __init__(self)


class Animal:
    def __init__(self,nombre,onomatopeya):
         self.nombre = nombre
         self.onomatopeya = onomatopeya

    def saludo(self):
        print("hola soy un",self.tipo, "y mi sonido es",self.onomatopeya)


class Gato(Animal):
    tipo = 'gato'
    #cuando creamos un metodo de init, el método de init de su clase padre no se va a ejecutar a menos que lo hagamos nosotros mismos 
    def __init__(self,nombre,onomatopeya):
        #para usar el init de la clase padre
        Animal.__init__(self,nombre,onomatopeya)
        print("Hola, soy un gato extendido")
        


class Perro(Animal):
    tipo = "perro"
    def __init__(self,nombre,onomatopeya):
        #super hace referencia a la clase padre, no se necesita pasar self en esta funcion
        super().__init__(nombre,onomatopeya)
        print("instanciando a perro")


class Leon(Animal):
    tipo = 'leon'


gato = Gato('Floffy','maullido')
gato.saludo()

perro = Perro('Tesla','ladrido')
perro.saludo()


leon = Leon('Simba','rugido')
leon.saludo()



