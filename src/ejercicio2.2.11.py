'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

def entrada():
    palabra = input("Introduce una plabra: ")
    return palabra

def deletreo(palabra):
    mensaje = []
    for letras in reversed(palabra):
        mensaje.append(letras)
    return mensaje

def main():

    #Entrada
    palabra = entrada()

    #Procesamiento
    salida = deletreo(palabra)

    #Salida
    print(salida)

if __name__ == "__main__":
    main()

