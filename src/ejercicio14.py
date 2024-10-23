'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
'''

def entrada():
    numero = int(input("Introduce un numero (escribe'0' para terminar): "))
    if numero >= 0:
        return numero
    else:
        raise ValueError("El número introducido no es entero positivo o 0")

def suma(numero):
    suma = 0
    while numero != 0: 
        suma = suma + numero
        numero = entrada()
    return suma
        
    
def main():
    
    #Entrada
    numero = entrada()

    #Procesamiento
    resultado = suma(numero)
    
    #Salida
    print(resultado)
    
if __name__ == "__main__":
    main()
