
'''
Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo 
que pueda aceptar una cadena y una letra como argumentos.

'''


# palabra = 'banana'
#contador = 0
#for letra in palabra:
#if letra == 'a':
#contador = contador + 1
#print(contador)

##PROCESO


def contar_letras(palabra, letra):
    cont = 0
    for l in palabra:
        if l == letra:
            cont += 1
    return cont


if __name__ == "__main__":

    #Entrada

    palabra = input("Escribe una frase: ")
    letra = input("Escribe una letra para contarla: ")

    ##SALIDA
    resultado = contar_letras(palabra,letra)

    print(resultado)