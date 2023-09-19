# Definir una lista para almacenar las frutas
frutas = []

# Función para calcular el costo total de un salpicón
def costo_total_salpicon():
    costo_total = 0
    for fruta in frutas:
        costo_total += fruta["precio_unitario"] * fruta["cantidad"]
    return costo_total

# Función para mostrar todas las frutas ordenadas por costo de mayor a menor
def mostrar_frutas_ordenadas():
    frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"], reverse=True)
    print("Frutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"{fruta['nombre']} - Precio Unitario: {fruta['precio_unitario']} - Cantidad: {fruta['cantidad']}")

# Función para mostrar la fruta más barata y la más cara
def mostrar_fruta_mas_barata_y_mas_cara():
    if not frutas:
        print("No se han ingresado frutas.")
        return
    
    frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"])
    fruta_mas_barata = frutas_ordenadas[0]
    fruta_mas_cara = frutas_ordenadas[-1]
    
    print(f"Fruta más barata: {fruta_mas_barata['nombre']} - Precio Unitario: {fruta_mas_barata['precio_unitario']}")
    print(f"Fruta más cara: {fruta_mas_cara['nombre']} - Precio Unitario: {fruta_mas_cara['precio_unitario']}")

# Solicitar al usuario la cantidad de frutas a ingresar
N = int(input("Ingrese la cantidad de frutas que desea ingresar: "))

# Pedir información de las frutas
for i in range(N):
    id_fruta = i + 1
    nombre = input(f"Nombre de la fruta {id_fruta}: ")
    precio_unitario = float(input(f"Precio unitario de {nombre}: "))
    cantidad = int(input(f"Cantidad de {nombre}: "))

    fruta = {
        "id": id_fruta,
        "nombre": nombre,
        "precio_unitario": precio_unitario,
        "cantidad": cantidad
    }

    frutas.append(fruta)

# Menú principal
while True:
    print("\nMenú de opciones:")
    print("1. Calcular costo total de un salpicón")
    print("2. Mostrar frutas ordenadas por costo")
    print("3. Mostrar fruta más barata y más cara")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "1":
        costo_total = costo_total_salpicon()
        print(f"El costo total del salpicón es: {costo_total}")
    elif opcion == "2":
        mostrar_frutas_ordenadas()
    elif opcion == "3":
        mostrar_fruta_mas_barata_y_mas_cara()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
