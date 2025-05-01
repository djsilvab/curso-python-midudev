numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero < 0:
            print("El número introducido no es positivo. Inténtalo de nuevo.")
    except ValueError:
        print("El valor introducido no es un número entero. Inténtalo de nuevo.")

print(f"El número introducido es: {numero}")