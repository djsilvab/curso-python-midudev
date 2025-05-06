print("\n Bucle for:")
frutas = ["manzana", "naranja", "plátano", "fresa"]
for fruta in frutas:
    print(fruta)

print("\n Bucle para cadena:")
cadena="david silva bazán"
for letra in cadena:
    print(letra)

#enumerate: devuelve el índice y el valor
print("\n Enumerate:")
ciudades = ["Madrid", "Barcelona", "Valencia"]
for indice, ciudad in enumerate(ciudades):
    print(f"Índice: {indice}, Ciudad: {ciudad}")


#bucles anidados:
letras = ["a", "b", "c"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra.upper()}-{numero}")

    
#compresión de listas:
print("\n Compresión de listas:")
cuadrados = [x**2 for x in range(10)]
print(cuadrados)
