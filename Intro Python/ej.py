## EJERCICIO DE MULTIPLICION
#a = 4 
#b = 8 
#res = 0 
#for x in range(a): 
#    res = res + b 
#print(res) 
#

### INGRESA NOMBRE Y APELLIDO Y LO DEVUELVE AL REVES

#
#a = input('ingresa nombre:')
#b = input('ingresa apellido:')
# 
#c = a+' '+b
#
#
#print(c[::-1])




#### ENCONTRAR EL MENOR NUMERO DE UNA LISTA

#lista = [5,-1,0,9,3]
#
#menor = 't'
#
#for x in lista:
#    if menor == 't':
#        menor = x
#    else:
#        menor = x if x < menor else menor
#
#
#
#print(menor)
#    
    
#### ESCRIBIR UNA FUNCION QUE DEVUELVA EL VOLUMEN DE UNA ESFERA POR SU RADIO
#import math
#
#def volumenEsfera(radio):
#    return ((4*math.pi*(radio**3))/3)
#
#volumen = volumenEsfera(6)
#print(volumen)
#


#### ESCRIBIR UNA FUNCION QUE DIGA SI EL USUARIO ES > EDAD

#def mayorEdad(usuario):
#    return usuario.edad > 17
#
#
#class Usuario:
#    def __init__(self,edad):
#        self.edad = edad
#
#
#
#usuario = Usuario(15)
#usuario2 = Usuario(21) 
#
#r1 = mayorEdad(usuario)
#r2 = mayorEdad(usuario2)
#
#print(r1,r2)
#

#### ESCRIBIR UNA FUNCION QUE INDIQUE SI UN NUMERO ES PAR O IMPAR

#def parImpar(numero):
#    return numero.par %2 == 0
#
#
#
#class Numero:
#    def __init__(self,par):
#        self.par = par 
#
#numero = Numero(11)
#re = parImpar(numero)
#
#print(re)
#

### ESCRIBIR UNA FUNCION QUE INDIQUE CUANTAS VOCALES TIENE UNA PALABRA
#a = 'ABraham'
#vocales = 0
#
#for x in a.lower():
#    vocales+=1 if x == 'a' or x == 'e' or x == 'i' or x =='o' or x == 'u' else 0
#print(vocales)
#


#### ESCRIBIR UNA APLICACION QUE RECIBA UNA CANTIDAD INIFINITA DE NUMEROS HASTA DECIR BASTA, LUEGO QUE DEVUELVA LA SUMA DE LOS NUMEROS INGRESADOS

######### FORMA 1 #############
#lista = [] 
#print('ingrese numeros y para salir escriba basta') 
#while True: 
#    x = input('ingresa un numero') 
#    if x != 'basta': 
#        try: 
#            x = int(x) 
#            lista += [x]
#        except:
#            print('dato invalido')
#            break
#    else:
#        break
#print(sum(lista))


######### FORMA 2 USANDO APPEND ############
#lista = [] 
#print('ingrese numeros y para salir escriba basta') 
#while True: 
#    x = input('ingresa un numero') 
#    if x != 'basta': 
#        try: 
#            x = int(x) 
#            lista.append(x)
#        except:
#            print('dato invalido')
#            break
#    else:
#        break
#
#resultado = 0
#
#for x in lista:
#    resultado += x
#
#print(resultado


########## ESCRIBIR UNA FUNCION QUE RECIBA NOMBRE Y AṔELLIDO Y LOS VAYA AGREGADNDO AUN ARCHIVO

#a => para ir agregando datos al archivo
def agregaNombreArchivo(nombre,apellido):
    c = open('nombrecompleto.txt','a')
    c.write(nombre + ' '+ apellido+'\n')
    c.close()

agregaNombreArchivo('jorge','castro')
agregaNombreArchivo('nicolas','castro')




