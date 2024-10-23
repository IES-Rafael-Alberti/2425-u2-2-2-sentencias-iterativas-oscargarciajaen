'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
'''

def entrada():
    numero = int(input("Introduce un número entero positivo: "))
    if numero > 0:
        return numero
    else:
        raise ValueError("El número introducido no es entero positivo")

def triangulo(numero):
    mensaje = []
    for i in range(1, numero + 1,2):
        mensaje_2 = []
        for x in range(i, 0, -2):
            mensaje_2.append(str(x))
        mensaje.append(" ".join(mensaje_2))

    return "\n".join(mensaje)

def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    salida = triangulo(numero)

    #Salida
    print(salida)

if __name__ == "__main__":
    main()
        