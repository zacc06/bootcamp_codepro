palabra_secreta = 'gatos'
intentos = 5

def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    cantidad_letras_de_palabra_a_encontrar = 5

    #creamos una lista vacia para almacenar el resultado
    letras_verificadas = []

    for posicion in range(cantidad_letras_de_palabra_a_encontrar): #5

        # es ogual el indice 0 de palabra_a_encontrar a indice 0 de palabra_ingresada?
        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]


        # la letra del indice 0 de palabra_ingresada en la palabra_a_encontrar
        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:
            # si se cumple guardamos en la lista de letras verificadas
            letras_verificadas.append('['+palabra_ingresada[posicion]+']')

        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append('('+palabra_ingresada[posicion]+')')

        else:
            letras_verificadas.append(palabra_ingresada[posicion])


    return letras_verificadas

while intentos > 0:
    print(f'te quedan {intentos} intentos')
    palabra = input(' ingrese una palabra')
    if palabra == palabra_secreta:
        print("Ganaste")
        break
    else:
        resultado = obtener_fila_verificada(palabra_secreta, palabra)
        print(resultado)
        intentos = intentos - 1
if intentos==0:
    print('ya no quedan intentos')