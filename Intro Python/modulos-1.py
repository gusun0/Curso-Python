#from modulos import saludo,mascotas 
#para renombrar un modulo se usa la palabra reservada as

import modulos as xs
from  camelcase import CamelCase 

print(xs.mascotas) 
xs.saludo('nicolas')

#GENERAMOS UNA INSTANCIA DE CAMELCASE

c = CamelCase()
s = 'esta oracion necesita CAMELCASE'

camelcased = c.hump(s)

print(camelcased) 




