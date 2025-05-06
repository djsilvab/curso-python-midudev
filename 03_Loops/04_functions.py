def sumar(a,b):
    return a + b

#Documentación de la función con docstring
def restar(a:int,b:int) -> int:
    """
    Función que resta dos números enteros.
    
    Parámetros:
    a (int): Primer número entero.
    b (int): Segundo número entero.
    
    Devuelve:
    int: La resta de a y b.
    """
    return a - b

#print(restar.__doc__)

help(restar)