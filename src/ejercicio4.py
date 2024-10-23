'''
Escribe un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atrás desde ese numero hasta 0 separado por comas.
'''

def entrada():
    numero = int(input("Introduce un número entero positivo: "))
    if numero > 0:
        return numero
    else:
        raise ValueError("El número introducido no es entero positivo")

def muestra(numero):
    solucion = ""
    numeros = []
    for i in range(numero, -1,-1):
        numeros.append(str(i))
    return ", ".join (numeros)
    
def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    salida = muestra(numero)

    #Salida
    print(salida)

if __name__ == "__main__":
    main()

