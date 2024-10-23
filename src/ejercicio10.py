'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.'''

def entrada():
    numero = int(input("Introduce un número entero: "))
    if numero <= 0:
        raise ValueError("El numero entero es negativo")
    return numero

def primo_o_no(numero):
    contador = 1
    contador_divisores = 0
    mensaje = ""
    for contador in range(1, numero + 1):
        if numero % contador == 0:
            contador_divisores += 1
            if contador_divisores == 1 or contador_divisores > 2:
                mensaje = "El número introducido no es primo."
            else:
                mensaje = "El número introducido es primo."
    return mensaje

def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    salida = primo_o_no(numero)

    #Salida
    print(salida)

if __name__ == "__main__":
    main()


            
     

