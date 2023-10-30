'''
Escribe un bucle while que comience con el último carácter en la cadena y 
haga un recorrido hacia atrás hasta el primer carácter en la cadena, 
imprimiendo cada letra en una línea independiente.

'''


##PROCESO

def dar_la_vuelta(cadena):
    cont = len(cadena)
    invertida = ''
    indice = cont - 1

    while indice >= 0:
        invertida += cadena[indice] + "\n"
        indice -= 1
    return invertida


if __name__ == "__main__":
    ##ENTRADA
    
    cadena = input("Escribe una palabra para darle la vuelta: ")

    ##SALIDA

    print(dar_la_vuelta(cadena))

    

