'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

def entrada():
    entrada = input("Introduce la contraseña: ")
    return entrada

def comprobación_de_contraseña(entrada):
    contrasena = "contraseña"  
    while entrada != contrasena:
        entrada = input("La contraseña es incorrecta, vuelve a intentarlo: ")
    mensaje = "Has introducido la contraseña correcta"
    return mensaje

def main():
    
    
    #Entrada 
    introduccion = entrada()

    #Procesamiento
    mensaje = comprobación_de_contraseña(introduccion)

    #Salida 
    print(mensaje)

if __name__ == "__main__":
    main()


    

    

