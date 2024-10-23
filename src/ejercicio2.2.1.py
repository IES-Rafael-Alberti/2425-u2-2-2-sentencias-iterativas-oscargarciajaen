'''
Escribir un programa que le pida al usuario una palabra y lo muestre por pantalla 10 veces.
'''

def entrada():
    palabra = input("Introduce una palabra: ")
    return palabra

def bucle(palabra): 
    solucion = ""

    for i in range(10):
        solucion = solucion + palabra + "\n"
    return solucion    


def main():

    #Entrada:
    palabra = entrada()
    #Procesamiento:
    salida = bucle(palabra)

    #Salida
    print(salida)

if __name__ == "__main__":
    main()
    