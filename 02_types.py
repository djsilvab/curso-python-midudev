
"""
    comentario
"""

###
#comentario
#otro comentario
###

import os
os.system("clear")

print(type(-5))

estado_civil : bool = False

#estado_civil = 33

edad = 18

if edad >= 18:
    print("Eres mayor de edad")

#operador ternario
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"

lista3: list[float | str | bool | int] = [3.12, "david", True, 1]
matrix = [[1,2],[2,3],[3,4],[4,5]]

print(lista3[-1])
print(lista3[0])
print(matrix[1][0])

#Slicing(rebanado)
print(lista3[1:-1])
print(lista3[1:])

lista = [1,2,3,4,5,6]
print(lista[1:4])

#Obtiene los 3 primeros números
print(lista[:3])
print(lista[:-1])
print(lista[:])#permite realizar una copia

#LISTA[INI:FIN:SALTO]
listax = list(range(1, 11))
print(listax)
print(listax[::2])
print(listax[::-1]) #reversa la lista

#Permite agregar elementos a la lista
listax += [11,12]
print(listax)
print("Longitud de la lista: ", len(listax))