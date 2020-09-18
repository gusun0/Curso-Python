# MANIPULANDO ARCHIVOS EN TXT

# creando variable para leer nuestro archivo
#el segundo argumento para es para ver los permisos que tiene el archivo
#r de read viene por defecto, lee el archivo
#append: a =>  nos permite agregar mas texto al final del archivo
# w, en dado caso de que el archivo no exista lo crea, y si existe, unicamente lo abre
# x sirve para crear archivos 


#c = open('archivo.txt','w')
#
#### PARA TENER ACCESO A CADA UNA DE LAS LINEAS QUE ESTAMOS LEYENDO
##for x in c:
##    print(x)
#
##### PARA AGREGAR ELEMENTOS AL TEXTO 
#c.write('agregaremos una nueva linea')
#c.write("\nagregando la linea numero 2")
#c.close()
#
#x = open('archivo.txt')
#print(x.read())
#
### READ LEE LA TOTALIDAD DEL ARCHIVO 
##
##print(c.readline())
##print(c.readline())
##print(c.readline())
##print(c.readline())




# PARA ELIMINAR ARCHIVOS se utiliza esta libreria/modulo del so
import os 

if (os.path.exists('archivo.txt')):
    os.remove('archivo.txt')
else:
    print("el archivo no existe")

#PARA ELIMINAR UN DIRECTORIO 
os.rmdir('micarpeta')










