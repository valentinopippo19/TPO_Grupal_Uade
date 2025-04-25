#CREAR UNA FUNCION QUE RECIBA UNA MATRIZ Y UN ELEMENTO QUE DESEA ELIMINAR DE ESTA
#Para hacer esto vamos a buscarlo con el ID, o por el Legajo
#Ya que cualquiera de las tres matrices posee ID, o Legajo

def eliminarElementoMatrizAlumnos(matriz,elemento):
    filas = len(matriz) #cantidad de filas
    columnas = len(matriz[0]) #cantidad de columnas
    for fil in range(filas):
        for col in range(columnas):
            if matriz[fil][col] == elemento:
                filaParaEliminar = fil
    matriz.pop(filaParaEliminar)
    print(matriz)

matriz = [[55,3,2],[66,3,0],[11,3,8]]
elemento = 11
eliminarElementoMatrizAlumnos(matriz,elemento)
