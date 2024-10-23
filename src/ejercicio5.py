'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

def entrada():
    cantidad = float(input("Introduce la cantidad que quiere invertir: "))
    interes_anual = float(input("Introduce el interes anual: "))
    anhos_inversion = int(input("Introduce el número de años que quiere invertir: "))
    if anhos_inversion <= 0:
        print("El numero de años tiene que ser un número entero positivo")
    return cantidad, interes_anual, anhos_inversion

def calculoCantidad(cantidad, interes_anual):
    cantidad = cantidad * (1 + interes_anual / 100)
    return cantidad

def generarSalida(cantidad, anhos_inversion, interes_anual):
    mensaje = ""
    contador = 1
    while contador <= anhos_inversion:
        cantidad = calculoCantidad(cantidad, interes_anual)
        mensaje += "Año " + str(contador) + "= " + str(calculoCantidad(cantidad, interes_anual)) + "\n"
        contador = contador + 1
    return mensaje

def salida(betis):
    print(betis)

def main():

    #Entrada
    cantidad, interes_anual, anhos_inversion = entrada()

    #Procesamiento
    calculoCantidad(cantidad, interes_anual)

    #Salida
    salida(generarSalida(cantidad, anhos_inversion, interes_anual))

if __name__ == "__main__":
    main()