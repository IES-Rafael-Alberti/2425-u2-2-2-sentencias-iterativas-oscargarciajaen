'''
Escribir un programa que le pida al usuario un número entero positivo y muestre por pantalla todos los impares desde uno hasta ese número separado por comas.
'''

def entrada():
    numero = int(input("Introduce un número entero positivo: "))
    if numero <= 0:
        print("El número no es un entero positivo.")
    return numero

def muestra(numero):
    solucion = ""
    for i in range(1, numero + 2,2):
        solucion = solucion + str(i) + ","
    solucion = solucion[:-1]    
    return solucion
    
def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    salida = muestra(numero)

    #Salida
    print(salida)

if __name__ == "__main__":
    main()

