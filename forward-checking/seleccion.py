#rows = [[4], [8], [10], [1, 1, 2, 1, 1], [1, 1, 2, 1, 1], [1, 6, 1], [6], [2, 2], [4], [2]]

#Recibe arreglo con valores de cuadrados a ingresar en filas
def seleccion(fila):
    #Arreglo con peso (suma) de cada fila
    j = len(fila)
    peso_fila = []
    for i in range(0, j, 1):
        numero = sum(fila[i])
        largo = len(fila[i])
        if largo > 0:
            numero = numero + largo -1
        peso_fila.append(numero)
    #print(peso_fila)

    #EVALUA DEL 10 AL 0
    #de izquierda a derecha
    filas_ordenadas = []
    for k in range(j, 0, -1):
        for fila in range(0, j, 1):
            if peso_fila[fila] == k:
                filas_ordenadas.append(fila)
    # print(filas_ordenadas)
    #Entrega arreglo con fila i a revisar en orden
    return filas_ordenadas

#seleccion(rows)