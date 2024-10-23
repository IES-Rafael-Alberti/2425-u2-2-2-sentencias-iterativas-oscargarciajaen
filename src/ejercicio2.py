'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido hasta su edad.
'''


def entrada():
    edad = int(input("Introduce tu edad: "))
    if edad > 0:
        return edad
    else: 
        raise ValueError("La edad introducida es 0 o menor")

def cadena(edad):
    solucion = ""

    for i in range(1, edad + 1):
        solucion = solucion + str(i) + "\n"
    return solucion    

def main():

    #Entrada
    edad = entrada()

    #Procesamiento
    salida = cadena(edad)

    #Salida
    print(salida)

if __name__ == "__main__":
    main()
    


