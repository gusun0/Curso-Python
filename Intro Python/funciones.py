# FUNCTIONS

def miFuncion():
    print("hola desde mi funcion")

#el *nombre se utiliza para pasar mas de un argumento
def imprimeDato(*nombre):
    print('mis argumentos son: ',nombre)


#imprimeDato('roberto','carlos','carlos','jaime')

def nombreCompleto(apellido,nombre):

    print(nombre,apellido)

#nombreCompleto(nombre="jorge",apellido="solis")

#keywordargs o argumento por llave usando sintaxis de diccioonario
def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

#nombreCompleto2(nombre="gusun0",apellido="gusun")

#funciones con argumentos por default 

def miFuncion2(argumento="Roberto"):
    print(argumento)

#miFuncion2('Batman')
#miFuncion2()

# FUNCION LISTA
def miFuncionLista(lista):
    for el in lista:
        print(el)

#miFuncionLista(['Roberto','Carlos','3'])


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i+el+' ' 
    return i

# cuando retornamos un valor tenemos que guardarlo en una variable
nombres = concatenaNombres(['roberto','carlos','3'])

#print(nombres)


def recursion(i):
    if(i<1):
        return i
    print(i)
    recursion(i-1)

recursion(3)
