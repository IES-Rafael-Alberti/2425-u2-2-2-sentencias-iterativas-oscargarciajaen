'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido
'''

def entrada():
    numero = int(input("Introduce un número entero positivo: "))
    return numero

def triangulo(numero):
    mensaje = []
    for i in range(1, numero + 1):
        mensaje.append("*" * i) 
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
        