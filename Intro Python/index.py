# un comentario
#if 3 > 5: # un comentario 
 #   print('esto no se imprime')

#if 3 < 5: # un comentario 
  #  print('si se cumple')  


x = 5
y = 'gusun0'

#print(x,y)

emailUser = 'gusun0@gusun0.com'
#print(emailUser)

#1 = 'hola'

a,b,c = 'curso','de','python'
#print(a,b,c) 

valor1 = valor2 = valor3 = 'Hola Mundo'
#print(valor1,valor2,valor3)


inicio = 'NR' 
final = 'MAL 2021'

#print(inicio+     final) 



word = 'Ceremonia' #string
word = "Corona Capital" #string

#print(word)

entero = 20 #integer
conDecimal = 20.2 #float

complejo = 2j+2 #complejo

#print(complejo)

lista = [1,2,3] 
#print(lista) 

lista.append(4)

#print(lista) 

lista2 = lista.copy()
#print(lista2)

lista.clear() 
#print(lista)


lista2.append(1)
#print(lista.count(22))
#print(lista2.count(1))


#cantidad de elementos de una lista

#print(lista2,len(lista2))


largoLista = len(lista)
largoLista2 = len(lista2)
#print(largoLista,largoLista2) 

#ACCEDIENDO A ELEMENTOS DE UNA LISTA

#print('elemento en la posicion 1 es: '+str(lista2[1])) 

#elimina el ultimo elemento de una lista
lista2.pop()
#print(lista2)



lista2.remove(1)
#print(lista2) 

#print(lista2)

lista2.append('hola')
#print(lista2)
lista2.reverse()


#print(lista2)
#print(lista2.sort())

lista.append(10)
lista.append(2)
lista.append(4)
lista.append(1)

#print(lista)

#print(sorted(lista))


li = [10,3,4,20] 
#print(li)

li_sorted = li.sort()
#print(li) 



#TUPĹAS
#print('TUPLAS')
tupla = ('Hola','soy','una','tupla')
#print(tupla)
#print(tupla.count('Hola'))
#print(tupla.index('Hola'))


tupla2 = tupla
tupla2 = list(tupla2)

tupla2.append('si')

#print(tupla2,sorted(tupla2))  



#RANGOS 

rango = range(6)
#print(rango)

#DICCIONARIOS


#UTILIZA KEYS

diccionario = {
        'nombre': 'Tesla',
        'raza': 'Persa',
        'edad': 5
        }

#print(diccionario['raza'])
#print(diccionario.get('nombre')) 
diccionario['nombre'] = 'Newton' 
#print(len(diccionario),diccionario) 

#agregando un nuevo elemento 

diccionario['ronronea'] = 'si' 
#print(diccionario) 


#FORMA 1 DE BORRAR ELEMENTOS 
#diccionario.pop('ronronea')
#print(diccionario) 

#FORMA 2 DE BORRAR 
#diccionario.popitem() 
#print(diccionario )


#FORMA 3 DE BORRAR CON FUNCION DEL 
del diccionario['ronronea']
#forma 1 de copíar un diccionario 
#copiaDiccionario = diccionario.copy() 

#FORMA NO 2 DE COPIAR UN DICCIONARIO
copiaDiccionario = dict(diccionario)
#para eliminar todos los datos de un diccionario 
diccionario.clear()
#print(diccionario,copiaDiccionario) 


#DICCIONARIOS ANIDADOS

fluffy = {
        "nombre": 'Fluffy',
        "edad": 4
}

mamba = {
        "nombre": 'Mamb',
        "edad":12
}



gatitos = {
        "Fluffy": fluffy,
        "Mamba": mamba
}        

print(gatitos)


perritos = dict(nombre="Tesla",edad="5")
print(perritos) 



#DATOS BOOLEANOS

verdadero  = True
falso = False
print(verdadero,falso)




