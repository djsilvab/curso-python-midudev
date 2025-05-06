#else , esta condición cuando se ejecuta
print("\n Bucle while con else")
cont = 0
while cont < 5:
    cont += 1

    if cont == 2:
        break

    print(cont)
else:
    print("El bucle ha terminado")

numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero < 0:
            print("El número introducido no es positivo. Inténtalo de nuevo.")
    except ValueError:
        print("El valor introducido no es un número entero. Inténtalo de nuevo.")

print(f"El número introducido es: {numero}")