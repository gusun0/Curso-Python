#dato = input("ingrese dato: ") 
#print (dato)
#lista = ['hola','mundo','cursos','feliz']
#if(lista.count(dato) >0):
#    print("el elemento se encuentra: ",dato)
#else:
#    print("ese elemento no se encuetra: ",dato)
#
#

#CALCULADORA QUE SOLAMENTE SUMA

n1 = input("Ingresa el primer numero: ")

try:
    n1 = int(n1)
except:
    n1 = 'hola'

if n1 == 'hola':
    print("el valor ingresado no es un entero")
    exit()

n2 = input("Ingresa el segundo numero: ")

try:
    n2 = int(n2)
except:
    n2 = 'hola'

if n2 == 'hola':
    print("el valor ingreado no es un entero")
    exit()

#if n1 == 'hola' or n2 == 'hola':
#    print('ingresaste mal los datos, prueba solo numeros')
#else:

simbolo = input("ingrese operacion:")
if(simbolo == '+'):
    print(n1+n2)
elif(simbolo == '-'):
    print(n1-n2)
elif(simbolo == '*'):
    print(n1*n2)
elif(simbolo == '/'):
    print(n1/n2)
else:
    print("el simbolo no es valido")

