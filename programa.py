# Función para imprimir la matriz
def imprimir_matriz(m, t="Matriz de datos"):
    print(f"\n{t.center(50, '=')}")
    if not m:
        print("(vacía)")
        return
    print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20))
    print("-" * 60)
    for i in range(len(m)):
        print(str(i).ljust(8), m[i][0].ljust(20), str(m[i][1]).ljust(10), m[i][2].ljust(20))

# Función para pedir índice válido
def pedir_indice(m):
    try:
        i = int(input("Ingresa el índice de la persona: "))
        if 0 <= i < len(m):
            return i
        else:
            print("Índice fuera de rango.")
    except:
        print("Índice inválido.")
    return None

# Función para modificar un dato
def modificar_dato(m):
    if not m: return m
    imprimir_matriz(m, "Modificar datos")
    i = pedir_indice(m)
    if i is not None:
        opciones = ["Nombre", "Nota", "Tema"]
        print("\n¿Qué deseas modificar?")
        for idx, op in enumerate(opciones, 1):
            print(f"{idx}. {op}")
        eleccion = input("Elige una opción (1/2/3): ")
        if eleccion in ["1", "2", "3"]:
            nuevo = input(f"Nuevo {opciones[int(eleccion)-1]}: ")
            m[i][int(eleccion)-1] = nuevo
        else:
            print("Opción no válida.")
    return m

# Función para eliminar la matriz
def eliminar_matriz(m):
    if not m: return m
    r = input("¿Deseas eliminar la matriz? (si/no): ").lower()
    if r == "si":
        imprimir_matriz(m, "Contenido antes de eliminar")
        m.clear()
        print("La matriz ha sido eliminada.")
    else:
        print("La matriz no fue eliminada.")
    return m

# Menú principal
def menu():
    matriz = []
    while True:
        print("\n" + "=" * 50)
        print("1. Ingresar nueva persona")
        print("2. Ver matriz")
        print("3. Modificar dato")
        print("4. Eliminar matriz")
        print("5. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            while True:
                nombre = input("Nombre (o 'salir' para cancelar): ")
                if nombre.lower() == "salir": break
                nota = input("Nota: ")
                tema = input("Tema: ")
                matriz.append([nombre, nota, tema])
                seguir = input("¿Ingresar otra persona? (si/no): ").lower()
                if seguir != "si":
                    break
        elif opcion == "2":
            imprimir_matriz(matriz)
        elif opcion == "3":
            modificar_dato(matriz)
        elif opcion == "4":
            eliminar_matriz(matriz)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

menu()
