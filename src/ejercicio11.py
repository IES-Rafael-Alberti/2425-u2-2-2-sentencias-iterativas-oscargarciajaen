'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

def entrada():
    palabra = input("Introduce una plabra: ")
    if palabra.isalpha():
        return palabra 
    else:
        raise ValueError("El valor introducido no es una palabra")

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

