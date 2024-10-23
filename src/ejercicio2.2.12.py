'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''
def entrada():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    return frase,letra

def numero_letras(frase, letra):
    contador = 0
    for letras in frase:
        if letra == letras:
            contador = contador + 1
    return contador

def main():
    #Entrada
    frase, letra = entrada()
    

    #Procesamiento
    salida = numero_letras(frase, letra)

    #Salida 
    print(salida)



if __name__ == "__main__":
    main()
