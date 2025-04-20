# Función para imprimir la matriz
imprimir_matriz = lambda m, t="Matriz de datos": (
    print(f"\n{t.center(50, '=')}") or
    (print("(vacía)") if not m else (
        print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20)),
        print("-" * 60),
        [print(str(i).ljust(8), m[i][0].ljust(20), str(m[i][1]).ljust(10), m[i][2].ljust(20)) for i in range(len(m))]
    ))
)


# Función para modificar un dato
def modificar_dato(m):
    imprimir_matriz(m, "Modificar datos")
    i = int(input("Ingresa el índice de la persona a modificar: "))
    if 0 <= i < len(m):
        print("\n¿Qué deseas modificar?\n1. Nombre\n2. Nota\n3. Tema")
        op = input("Elige una opción (1/2/3): ")
        nuevo = input("Nuevo valor: ")
        if op in ["1", "2", "3"]:
            m[i][int(op)-1] = nuevo
        else:
            print("Opción no válida.")
    else:
        print("Índice fuera de rango.")
    return m

# Función para eliminar la matriz
def eliminar_matriz(m):
    if input("\n¿Deseas eliminar la matriz? (si/no): ").lower() == "si":
        imprimir_matriz(m, "Contenido antes de eliminar")
        m.clear()
        print("\nLa matriz ha sido eliminada.")
    else:
        print("\nLa matriz no fue eliminada.")
    return m

# === Flujo principal ===
matriz_datos = [[input("Nombre: "), input("Nota: "), input("Tema: ")] 
                for _ in iter(lambda: input("\n¿Deseas ingresar una persona? (si/no): ").lower() == "si", False)]

# Mostrar la matriz original
imprimir_matriz(matriz_datos, "Matriz original")

# Modificar datos
matriz_datos = modificar_dato(matriz_datos)

# Mostrar la matriz modificada
imprimir_matriz(matriz_datos, "Matriz modificada")

# Eliminar matriz
matriz_datos = eliminar_matriz(matriz_datos)

# Mostrar estado final
imprimir_matriz(matriz_datos, "Estado final de la matriz")