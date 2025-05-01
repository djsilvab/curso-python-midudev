
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

#Añadir un elemento al final de la lista
listax.append(13)
print("Longitud de la lista: ", len(listax))

#Insertar un elemento en una posición específica
print(listax)
listax.insert(4, "X")
print(listax)

#Agregar varios elementos al final de la lista
listax.extend([14,15])
print(listax)

#Elimina la primera coincidencia del elemento
listax.remove('X')
print(listax)

#Elimina el último elemento de la lista
listax.pop() # Equivalente al último indice => listax.pop(-1)
print(listax)

#Eliminar el segundo elemento de la lista
listax.pop(1)
print(listax)

#Eliminar un valor específico de la lista
del listax[-1] #Elimina el segundo elemento de la lista

#Eliminar todos los elementos de la lista
listax.clear()
print(listax)

#Eliminar un rango de elementos de la lista
del listax[1:3]

#Ordenar una lista modificando la original
listax = [4, 3, 2, 5, 1]
print(listax)
listax.sort() #Ordena de menor a mayor
print(listax)

numbers = [4, 3, 2, 5, 1]
sorted_numbers = sorted(numbers) #Ordena de menor a mayor pero no modifica la original
print(numbers)

frutas = ["banana", "kiwi", "mango", "Limón" ,"manzana", "Pera"]
frutas.sort(key=str.lower) #Ordena de menor a mayor sin importar mayúsculas o minúsculas
print(frutas)

frutas += ["aguacate", "sandía", "papaya", "banana"]
print(frutas.count("banana"))
print("papaya" in frutas)

#Bucle con una simple de condición
cont = 0
while cont < 5:
    print("Contador: ", cont)
    cont += 1


