'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''

def entrada():
    palabra = input("Introduce una palabra (escribe'salir' para terminar): ")
    return palabra

def eco(palabra):
    while palabra != "salir":
        print(palabra)
        palabra = entrada()
    
def main():
    
    #Entrada
    palabra = entrada()

    #Procesamiento
    eco(palabra)
    
if __name__ == "__main__":
    main()
