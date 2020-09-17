#if 2 < 5:
#    print("2 es menor que 5")
#if 2 == 2:
#    print("2 igual a 2")
#if 2 == 3:
#    print("2 igual a 3")
#
#if 2 > 5:
#    print("2 es mayor que 5")
#
#if 3 != 2:
#    print("3 es distinto a 2")


#IF ELIF ELSE

if 2 > 5:
    print("dos es menor que 5 en if")
elif 2 > 5:
    print("2 es menor que 5 en elif")
elif 2 < 5:
    print("2 es menor que 5 en elif")
else:
    print("solo si if y elif entregan falsos")

#IF Y OPERADORES TERNARIOS

print("cuando devuelve true") if 5 > 2 else print("cuando devuelve false") 



# AND y OR
if 2 < 5 and 3 < 2:
    print("hay una falsa, no se muestra")

if 2 < 5 or 3 < 2:
    print("al menos hay un true")

