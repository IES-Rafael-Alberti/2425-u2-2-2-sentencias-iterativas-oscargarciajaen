'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido hasta su edad.
'''


def entrada():
    edad = int(input("Introduce tu edad: ")) 
    return edad

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
    


