import mysql.connector

#RECIBE 4 PARAMETROS
# HOST => ES LA MAQUINA EN DONDE VAMOS A TRABAJAR
# USER => USUARIO QUE VAMOS A UTULIZAR PARA CONECTAROS
#PASSWORD => CONTRASEÑA QUE USAMOS PARA CONECTARNOS
midb = mysql.connector.connect(
    host = 'localhost',
    user = 'chanchitofeliz',
    password = '123456',
    database = 'prueba'
)

# UN CURSOS ES UN OBJETO QUE NOS PERMITE INTERACTURA CON LA BD MEDIANTE SQL
cursor = midb.cursor()


### PARA INGRESAR DATOS ####
# primero escribimos la consulta que queremos escribir 




# listar datos

# FETCHALL DEVUELVE LAS INSTANCIAS DE TODOS LOS OBJETOS QUE ENCONTRO EN LA BD

#cursor.execute('select * from Usuario') 
#resultado = cursor.fetchall()       
#print(resultado)


### PARA LIMITAR LA SALIDA DE LOS DATOS DE LA BD

cursor.execute('select * from Usuario limit 2')
resultado = cursor.fetchall()        
print(resultado)



# ver definiciones de tablas
# cursor.execute('show create table Usuario')


### INGRESAR DATOS ###
#sql = 'insert into Usuario (email,username,edad) values(%s, %s,%s)'                                         
#values = ('micorreo@correo.co.nz','gusun3',40)



### UPDATE DATOS EN MYSQL
# HACEMOS CONSULTA DE MYSQL

#sql = 'update Usuario set email = %s where id = %s'
#values = ('correo@correo.mx', 2);
#cursor.execute(sql,values)

##el metodo de commit toma los datos y ejecuta la consulta contra la db
#midb.commit()

#print(cursor.rowcount)

#print(resultado)


##### ELMINAR DATOS #####

#sql = 'delete from Usuario where id = %s'
#values = (2, )
#cursor.execute(sql,values)
#midb.commit() 




