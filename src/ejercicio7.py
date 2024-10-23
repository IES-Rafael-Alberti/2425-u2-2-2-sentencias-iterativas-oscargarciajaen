'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

def tabla():
    tablas = []
    for i in range(11):
        tablas.append("Esta es la tabla de multiplicar del número " + str(i) + " ")
        for calculo in range(11):
            tablas.append( str(i) + "x" +  str(calculo) + "=" +  str(i * calculo) + " " )
    return "\n".join(tablas)

#Procesamiento
salida = tabla()

#Salida 
print(tabla())

