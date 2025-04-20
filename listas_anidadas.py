# Función lambda para imprimir la matriz
imprimir_matriz = lambda m, t="Matriz de datos": (
    print(f"\n{t.center(50, '=')}") or
    (print("(vacía)") if not m else (
        print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20)),
        print("-" * 60),
        [print(str(i).ljust(8), *[str(e).ljust(w) for e, w in zip(m[i], [20, 10, 20])]) for i in range(len(m))]
    ))
)

# Lambda para pedir índice válido
pedir_indice = lambda m: (
    int(input("Ingresa el índice de la persona: ")) if m and (
        (lambda i: 0 <= i < len(m))(int(input("Ingresa el índice de la persona: ")))
    ) else None
)

# Función para modificar un dato (con validación y lambda interna)
def modificar_dato(m):
    if not m: return m
    imprimir_matriz(m, "Modificar datos")
    try:
        i = int(input("Índice a modificar: "))
        if not (0 <= i < len(m)): return print("Índice fuera de rango.") or m
        campos = ["Nombre", "Nota", "Tema"]
        print("\n".join([f"{j+1}. {c}" for j, c in enumerate(campos)]))
        op = input("Opción (1/2/3): ")
        if op in ["1", "2", "3"]:
            m[i][int(op)-1] = input(f"Nuevo {campos[int(op)-1]}: ")
        else:
            print("Opción no válida.")
    except:
        print("Entrada inválida.")
    return m

# Función para eliminar la matriz
eliminar_matriz = lambda m: (
    (imprimir_matriz(m, "Contenido antes de eliminar") or m.clear() or print("Matriz eliminada."))
    if input("¿Eliminar la matriz? (si/no): ").lower() == "si" else print("Matriz no eliminada.")
) or m

# === Menú principal optimizado ===
def menu():
    matriz = []
    while True:
        print("\n" + "=" * 50)
        print("1. Ingresar nueva persona")
        print("2. Ver matriz")
        print("3. Modificar dato")
        print("4. Eliminar matriz")
        print("5. Salir")
        op = input("Elegí una opción: ").strip()

        if op == "1":
            while True:
                nombre = input("Nombre (o 'salir' para volver): ")
                if nombre.lower() == "salir": break
                nota = input("Nota: ")
                tema = input("Tema: ")
                matriz.append([nombre, nota, tema])
                if input("¿Agregar otra? (si/no): ").lower() != "si": break

        elif op == "2":
            imprimir_matriz(matriz)

        elif op == "3":
            modificar_dato(matriz)

        elif op == "4":
            eliminar_matriz(matriz)

        elif op == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")

menu()
