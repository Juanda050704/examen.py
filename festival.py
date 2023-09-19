bandas = []

def registrar_banda():
    id_banda = len(bandas) + 1
    nombre = input("Nombre de la banda: ")
    genero = input("Género musical: ")
    hora_presentacion = input("Hora de presentación (H:M:S): ")
    pago = float(input("Pago a la banda: "))
    estado = input("¿Ya se presentó? (Sí/No): ").lower() == "sí"
    banda = {
        "id": id_banda,
        "nombre": nombre,
        "genero": genero,
        "hora_presentacion": hora_presentacion,
        "pago": pago,
        "estado": estado
    }
    bandas.append(banda)
    print(f"Banda {nombre} registrada con éxito.")


def mostrar_bandas_no_presentada () :
    print("Bandas que no se han presentado: , ")
    for banda in bandas:
        if not banda["estado"]:
            print(f"{banda['id']}: {banda['nombre']} - {banda['genero']} - {banda['hora_presentacion']}")

 def mostrar_bandas_presentadas():
    print("Bandas que ya se presentaron:")
    for banda in bandas:
        if banda["estado"]:
            print(f"{banda['id']}: {banda['nombre']} - {banda['genero']} - {banda['hora_presentacion']}")


def cambiar_hora_presentacion():
    id_banda = int(input("Ingrese el ID de la banda a la que desea cambiar la hora de presentación: "))
    for banda in bandas:
        if banda["id"] == id_banda and not banda["estado"]:
            nueva_hora = input("Ingrese la nueva hora de presentación (H:M:S): ")
            banda["hora_presentacion"] = nueva_hora
            print(f"La hora de presentación de {banda['nombre']} ha sido actualizada.")
            return
    print("No se encontró una banda con el ID especificado o ya se ha presentado.")

def retirar_banda():
    id_banda = int(input("Ingrese el ID de la banda que desea retirar: "))
    for banda in bandas:
        if banda["id"] == id_banda and not banda["estado"]:
            bandas.remove(banda)
            print(f"{banda['nombre']} ha sido retirada del listado de bandas.")
            return
    print("No se encontró una banda con el ID especificado o ya se ha presentado.")

# Menú principal
while True:
    print("\nMenú de opciones:")
    print("1. Registrar una banda")
    print("2. Mostrar bandas no presentadas")
    print("3. Cambiar hora de presentación")
    print("4. Retirar una banda")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "1":
        registrar_banda()
    elif opcion == "2":
        mostrar_bandas_no_presentadas()
    elif opcion == "3":
        cambiar_hora_presentacion()
    elif opcion == "4":
        retirar_banda()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
