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


personas = ["david", "aldo", "lourdes", "walter"]
for idx,pers in enumerate(personas):
    if pers == "aldo": continue
    print(f"[{idx}]=>{pers.upper()}")

#compresion de listas
print("\n Listas comprimidas")
animales = ["perro","gato","raton","loro","pez","canario"]
animales_may = [ animal.upper() for animal in animales]
print(animales_may)

#Muestra los números pares de una lista
pares = [n for n in range(13) if n % 2 == 0]
print(pares)